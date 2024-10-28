from typing import (
    _SpecialForm,
    Annotated,
    Any,
    Literal,
    Optional,
    Self,
    TypeVar,
    Union,
    get_origin as get_generic_origin,
    get_args as get_generic_args
)

from pydantic import BaseModel, Field
from pydantic.fields import FieldInfo

from .deserialization import (
    Context,
    DeserializationError,
    Next,
    ProgressiveDeserializer,
    Record,
    Replay,

    deserialize,
    deserialize_base_model
)

from .token import Eol, Token, Word


__all__ = (
    "Command",
    "CommandArgumentBindingError",
    "Key",
    "Subcommand",

    "deserialize_command"
)


M = TypeVar("M", bound=BaseModel)


class CommandArgumentBindingError(DeserializationError):
    pass


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
    if get_generic_origin(hint) is Annotated:
        return _is_subcommand_hint(get_generic_args(hint)[0])

    return get_generic_origin(hint) is list and \
        _is_command_hint(get_generic_args(hint)[0])


def _is_subcommand_field(field: FieldInfo) -> bool:
    return _is_subcommand_hint(field.annotation)


def _get_regular_fields(hint: type[M]) -> dict[str, FieldInfo]:
    return {
        name: field
        for name, field in hint.model_fields.items()
        if not _is_subcommand_field(field)
    }


def _get_subcommand_defaults(hint: type[M]) -> dict[str, list[Any]]:
    return {
        name: []
        for name, field in _get_subcommand_fields(hint).items()
    }


def _get_subcommand_fields(hint: type[M]) -> dict[str, FieldInfo]:
    return {
        name: field
        for name, field in hint.model_fields.items()
        if _is_subcommand_field(field)
    }


def _extract_command_hint(hint: Any) -> Any:
    if get_generic_origin(hint) is Annotated:
        return _extract_command_hint(get_generic_args(hint)[0])

    return get_generic_args(hint)[0]


def _get_subcommand_field_name(
    fields: dict[str, FieldInfo],
    subcommand: Command
) -> str:
    for name, field in fields.items():
        if isinstance(subcommand, _extract_command_hint(field.annotation)):
            return name

    raise TypeError


def _seek(hint: type[Token]) -> ProgressiveDeserializer[None]:
    index = yield Record()

    while True:
        token = yield Next()

        if not isinstance(token, hint):
            index = yield Record()
            continue

        break

    yield Replay(index=index)


def deserialize_command(
    parent_hints: tuple[type[Command], ...],
    strict: bool = True,
    context: Optional[Context] = None
) -> ProgressiveDeserializer[tuple[Optional[Command], bool]]:
    try:
        yield from _seek(Word)
    except EOFError:
        return None, True

    parent = None

    try:
        if not parent_hints:
            raise DeserializationError

        parent = yield from deserialize(Union[parent_hints], context=context)
    except DeserializationError:
        if strict:
            raise

        try:
            yield from _seek(Eol)
        except EOFError:
            pass

    try:
        token = yield Next()

        if not isinstance(token, Eol):
            if not strict:
                return None, False

            raise CommandArgumentBindingError
    except EOFError:
        return parent, True

    if not parent:
        return parent, False

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
                strict=True,
                context=context
            )
        except DeserializationError:
            yield Replay(index=index)
            break

        if not child:
            break

        name = _get_subcommand_field_name(child_fields, child)
        children[name].append(child)

    parent = parent.model_copy(update=children)

    return parent, eof


@_SpecialForm # type: ignore[call-arg]
def Key(self, parameters):
    if not isinstance(parameters, tuple):
        parameters = (parameters,)

    return Annotated[
        tuple[tuple(Literal[parameter] for parameter in parameters)],
        Field(default=tuple(parameters))
    ]


@_SpecialForm # type: ignore[call-arg]
def Subcommand(self, parameter):
    return Annotated[
        list[parameter],
        Field(default_factory=list)
    ]
