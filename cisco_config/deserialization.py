from ipaddress import IPv4Address

from typing import (
    Annotated,
    Any,
    Generator,
    Literal,
    Optional,
    Protocol,
    Self,
    Union,
    get_args as get_generic_args,
    get_origin as get_generic_origin,
    runtime_checkable
)

from pydantic import BaseModel, TypeAdapter, ValidationError

from .token import Word


__all__ = (
    "Context",
    "Cut",
    "Deserializable",
    "Next",
    "ProgressiveDeserializer",
    "ProgressiveDeserializerRequest",
    "Record",
    "Replay",

    "deserialize",
    "deserialize_annotated",
    "deserialize_base_model",
    "deserialize_dictionary",
    "deserialize_float",
    "deserialize_integer",
    "deserialize_ipv4_address",
    "deserialize_literal",
    "deserialize_none",
    "deserialize_string",
    "deserialize_union"
)


class Cut(BaseModel):
    pass


class Next(BaseModel):
    pass


class Record(BaseModel):
    pass


class Replay(BaseModel):
    index: int


type ProgressiveDeserializerRequest = Union[Cut, Next, Record, Replay]
type ProgressiveDeserializer[T] = Generator[
    ProgressiveDeserializerRequest,
    Any,
    T
]


Context = dict[str, Any]


@runtime_checkable
class Deserializable(Protocol):

    @classmethod
    def deserialize(
        cls,
        context: Optional[Context] = None
    ) -> ProgressiveDeserializer[Self]:
        ...


def deserialize_string() -> ProgressiveDeserializer[str]:
    token = yield Next()

    if not isinstance(token, Word):
        raise ValueError

    return token.value


def deserialize_ipv4_address() -> ProgressiveDeserializer[IPv4Address]:
    return IPv4Address((yield from deserialize_string()))


def deserialize_literal(
    members: tuple[str, ...]
) -> ProgressiveDeserializer[str]:
    result = yield from deserialize_string()

    if result not in members:
        raise ValueError

    return result


def deserialize_integer() -> ProgressiveDeserializer[int]:
    return int((yield from deserialize_string()))


def deserialize_float() -> ProgressiveDeserializer[float]:
    return float((yield from deserialize_string()))


def deserialize_none() -> ProgressiveDeserializer[None]:
    yield from ()
    return None


def deserialize_union(
    members: tuple[type[Any], ...],
    context: Optional[Context] = None
) -> ProgressiveDeserializer[Any]:
    index = yield Record()
    reason = None

    for member in members:
        try:
            return (yield from deserialize(member, context=context))
        except (ValueError, EOFError) as error:
            reason = error

            yield Replay(index=index)

    raise ValueError from reason


def deserialize_dictionary(
    hints: dict[str, type[Any]],
    context: Optional[Context] = None
) -> ProgressiveDeserializer[dict]:
    result = {}

    for name, hint in hints.items():
        result[name] = yield from deserialize(hint, context=context)

    return result


def deserialize_base_model(
    hint: type[BaseModel],
    fields: Optional[dict[str, type[Any]]] = None,
    defaults: dict[str, Any] = {},
    context: Optional[Context] = None
) -> ProgressiveDeserializer[BaseModel]:
    if not fields:
        fields = {
            name: field.annotation
            for name, field in hint.model_fields.items()
        }

    data = yield from deserialize_dictionary(fields, context=context)

    try:
        result = hint.model_validate({**defaults, **data}, context=context)
    except ValidationError as error:
        raise ValueError from error

    return result


def deserialize_annotated(
    hint: type[Annotated],
    context: Optional[Context] = None
) -> ProgressiveDeserializer[Any]:
    member = get_generic_args(hint)[0]

    result = (yield from deserialize(member, context=context))

    try:
        validated = TypeAdapter(hint).validate_python(result, context=context)
    except ValidationError as error:
        raise ValueError from error

    return validated


def deserialize(
    hint: type[Any],
    context: Optional[Context] = None
) -> ProgressiveDeserializer[Any]:
    if get_generic_origin(hint) is Annotated:
        return (yield from deserialize_annotated(hint, context=context))
    elif get_generic_origin(hint) is Literal:
        members = get_generic_args(hint)

        return (yield from deserialize_literal(members))
    elif get_generic_origin(hint) is Union:
        members = get_generic_args(hint)

        return (yield from deserialize_union(members, context=context))
    elif issubclass(hint, Deserializable):
        return (yield from hint.deserialize(context=context))
    elif issubclass(hint, BaseModel):
        return (yield from deserialize_base_model(hint, context=context))
    elif hint is str:
        return (yield from deserialize_string())
    elif hint is int:
        return (yield from deserialize_integer())
    elif hint is float:
        return (yield from deserialize_float())
    elif hint is IPv4Address:
        return (yield from deserialize_ipv4_address())
    elif hint is type(None):
        return (yield from deserialize_none())
    else:
        raise TypeError
