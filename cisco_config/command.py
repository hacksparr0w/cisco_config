from typing import (
    Any,
    Optional,
    Self,
    Union,
    get_origin as get_generic_origin,
    get_args as get_generic_args
)

from pydantic import BaseModel
from pydantic.fields import FieldInfo

from .deserialization import (
    Context,
    Cut,
    Next,
    ProgressiveDeserializer,
    Record,
    Replay,

    deserialize,
    deserialize_base_model
)

from .token import Eol, Word


__all__ = (
    "Command",

    "deserialize_command"
)


class Command(BaseModel):
    @classmethod
    def deserialize(
        cls,
        context: Optional[Context] = None
    ) -> ProgressiveDeserializer[Self]:
        return deserialize_base_model(
            cls,
            fields=_get_regular_fields(cls),
            defaults=_get_subcommand_defaults(cls),
            context=context
        )


def _is_command_hint(hint: Any) -> bool:
    if get_generic_origin(hint) is Union:
        return any(_is_command_hint(arg) for arg in get_generic_args(hint))

    return issubclass(hint, Command)


def _is_subcommand_hint(hint: Any) -> bool:
    return get_generic_origin(hint) is list and \
        _is_command_hint(get_generic_args(hint)[0])


def _is_subcommand_field(field: FieldInfo) -> bool:
    return _is_subcommand_hint(field.annotation)


def _get_regular_fields[T: BaseModel](hint: type[T]) -> dict[str, FieldInfo]:
    return {
        name: field
        for name, field in hint.model_fields.items()
        if not _is_subcommand_field(field)
    }


def _get_subcommand_defaults[T: BaseModel](
    hint: type[T]
) -> dict[str, list[Any]]:
    return {
        name: []
        for name, field in _get_subcommand_fields(hint).items()
    }


def _get_subcommand_fields[T: BaseModel](
    hint: type[T]
) -> dict[str, FieldInfo]:
    return {
        name: field
        for name, field in hint.model_fields.items()
        if _is_subcommand_field(field)
    }


def _extract_command_hint(hint: Any) -> Any:
    return get_generic_args(hint)[0]


def _get_subcommand_field_name(
    fields: dict[str, FieldInfo],
    subcommand: Command
) -> str:
    for name, field in fields.items():
        if isinstance(subcommand, _extract_command_hint(field.annotation)):
            return name

    raise TypeError


def _seek() -> ProgressiveDeserializer[None]:
    index = yield Record()

    while True:
        token = yield Next()

        if not isinstance(token, Word):
            yield Cut()
            index = yield Record()
            continue

        break

    yield Cut()
    yield Replay(index=index)


def deserialize_command(
    parent_hints: tuple[type[Command], ...],
    context: Optional[Context] = None
) -> ProgressiveDeserializer[tuple[Optional[Command], bool]]:
    try:
        yield from _seek()
    except EOFError:
        return None, True

    parent = yield from deserialize(Union[parent_hints], context=context)

    yield Cut()

    try:
        token = yield Next()

        if not isinstance(token, Eol):
            raise RuntimeError
    except EOFError:
        return parent, True

    parent_hint = type(parent)
    child_fields = _get_subcommand_fields(parent_hint)

    if not child_fields:
        return parent, False

    child_hints = tuple(
        _extract_command_hint(field.annotation)
        for field in child_fields.values()
    )

    children = _get_subcommand_defaults(parent_hint)
    eof = False

    while True:
        index = yield Record()

        try:
            child, eof = yield from deserialize_command(
                child_hints,
                context=context
            )
        except ValueError:
            yield Replay(index=index)
            break

        if not child:
            break

        name = _get_subcommand_field_name(child_fields, child)
        children[name].append(child)

    parent = parent.copy(update=children)

    yield Cut()

    return parent, eof
