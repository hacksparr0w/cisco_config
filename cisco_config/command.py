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
    def deserialize(cls) -> ProgressiveDeserializer[Self]:
        fields = {
            name: field.annotation
            for name, field in _get_regular_fields(cls).items()
        }

        defaults = _get_subcommand_defaults(cls)

        return deserialize_base_model(cls, fields, defaults)


def _is_list_subcommand_hint(hint: type) -> bool:
    return get_generic_args(hint) is list \
        and get_generic_args(hint) == (Command,)


def _is_optional_subcommand_hint(hint: type) -> bool:
    return get_generic_origin(hint) is Union and \
        get_generic_args(hint) == (Command, type(None))


def _is_subcommand_hint(hint: type) -> bool:
    return _is_list_subcommand_hint(hint) or \
        _is_optional_subcommand_hint(hint)


def _get_subcommand_default(info: FieldInfo) -> Any:
    if _is_list_subcommand_hint(info.annotation):
        return []

    if _is_optional_subcommand_hint(info.annotation):
        return None

    raise TypeError


def _get_regular_fields(hint: type) -> dict[str, FieldInfo]:
    return {
        name: field
        for name, field in hint.model_fields.items()
        if not _is_subcommand_hint(field.annotation)
    }


def _get_subcommand_fields(hint: type[BaseModel]) -> dict[str, FieldInfo]:
    return {
        name: field
        for name, field in hint.model_fields.items()
        if _is_subcommand_hint(field.annotation)
    }


def _get_subcommand_defaults(hint: type[BaseModel]) -> dict[str, Any]:
    return {
        name: _get_subcommand_default(field)
        for name, field in _get_subcommand_fields(hint).items()
    }


def _get_subcommand_hint_base(hint: type) -> type[Command]:
    return get_generic_args(hint)[0]


def _get_subcommand_name_mapping(
    hint: type[BaseModel]
) -> dict[type[Command], str]:
    return {
        _get_subcommand_hint_base(field.annotation): name
        for name, field in _get_subcommand_fields(hint).items()
    }


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
    hints: tuple[type[Command], ...]
) -> ProgressiveDeserializer[tuple[Optional[Command], bool]]:
    try:
        yield from _seek()
    except EOFError:
        return None, True

    parent = yield from deserialize(Union[hints])

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

    child_names = _get_subcommand_name_mapping(parent_hint)
    child_hints = (
        _get_subcommand_hint_base(field.annotation)
        for field in child_fields.values()
    )

    children = _get_subcommand_defaults(parent_hint)
    eof = False

    while True:
        index = yield Record()

        try:
            child, eof = yield from deserialize_command(child_hints)
        except ValueError:
            yield Replay(index=index)
            break

        if not child:
            break

        name = child_names[type(child)]
        field = child_fields[name]

        if _is_list_subcommand_hint(field.annotation):
            children[name].append(child)
        elif _is_optional_subcommand_hint(field.annotation):
            children[name] = child
        else:
            raise TypeError

    parent = parent.copy(update=children)

    yield Cut()

    return parent, eof
