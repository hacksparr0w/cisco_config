from ipaddress import IPv4Address

from typing_extensions import TypeAliasType
from typing import (
    Annotated,
    Any,
    Generator,
    Literal,
    Optional,
    Protocol,
    Self,
    TypeAlias,
    TypeVar,
    Union,
    get_args as get_generic_args,
    get_origin as get_generic_origin,
    runtime_checkable
)

from pydantic import BaseModel, TypeAdapter, ValidationError
from pydantic.fields import FieldInfo

from .token import Word


__all__ = (
    "Context",
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


T = TypeVar("T")
M = TypeVar("M", bound=BaseModel)


class Next(BaseModel):
    pass


class Record(BaseModel):
    pass


class Replay(BaseModel):
    index: int


ProgressiveDeserializerRequest: TypeAlias = Union[Next, Record, Replay]
ProgressiveDeserializer: TypeAlias = Generator[
    ProgressiveDeserializerRequest,
    Any,
    T
]


Context = dict[str, Any]


class DeserializationError(Exception):
    pass


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
        raise DeserializationError

    return token.value


def deserialize_ipv4_address() -> ProgressiveDeserializer[IPv4Address]:
    try:
        return IPv4Address((yield from deserialize_string()))
    except ValueError as error:
        raise DeserializationError from error


def deserialize_literal(
    members: tuple[str, ...]
) -> ProgressiveDeserializer[str]:
    result = yield from deserialize_string()

    if result not in members:
        raise DeserializationError

    return result


def deserialize_integer() -> ProgressiveDeserializer[int]:
    try:
        return int((yield from deserialize_string()))
    except ValueError as error:
        raise DeserializationError from error


def deserialize_float() -> ProgressiveDeserializer[float]:
    try:
        return float((yield from deserialize_string()))
    except ValueError as error:
        raise DeserializationError from error


def deserialize_none() -> ProgressiveDeserializer[None]:
    yield from ()
    return None


def deserialize_union(
    members: tuple[Any, ...],
    context: Optional[Context] = None
) -> ProgressiveDeserializer[Any]:
    index = yield Record()
    reason = None

    for member in members:
        try:
            return (yield from deserialize(member, context=context))
        except (DeserializationError, EOFError) as error:
            reason = error

            yield Replay(index=index)

    raise DeserializationError from reason


def deserialize_tuple(
    members: tuple[Any, ...],
    context: Optional[Context] = None
) -> ProgressiveDeserializer[tuple[Any, ...]]:
    result = []

    for member in members:
        item = yield from deserialize(member, context=context)
        result.append(item)

    return tuple(result)


def deserialize_dictionary(
    hints: dict[str, Any],
    context: Optional[Context] = None
) -> ProgressiveDeserializer[dict[str, Any]]:
    result = {}

    for name, hint in hints.items():
        result[name] = yield from deserialize(hint, context=context)

    return result


def deserialize_base_model(
    hint: type[M],
    fields: Optional[dict[str, FieldInfo]] = None,
    defaults: dict[str, Any] = {},
    context: Optional[Context] = None
) -> ProgressiveDeserializer[M]:
    if not fields:
        fields = {
            name: field
            for name, field in hint.model_fields.items()
        }

    hints = {name: field.annotation for name, field in fields.items()}
    data = yield from deserialize_dictionary(hints, context=context)

    try:
        result = hint.model_validate(
            {
                **defaults,
                **data
            },
            context=context
        )
    except ValidationError as error:
        raise DeserializationError from error

    return result


def deserialize_annotated(
    hint: Any,
    context: Optional[Context] = None
) -> ProgressiveDeserializer[Any]:
    member = get_generic_args(hint)[0]

    result = (yield from deserialize(member, context=context))

    try:
        validated = TypeAdapter(hint) \
            .validate_python(result, context=context)
    except ValidationError as error:
        raise DeserializationError from error

    return validated


def deserialize(
    hint: Any,
    context: Optional[Context] = None
) -> ProgressiveDeserializer[Any]:
    if get_generic_origin(hint) is Annotated:
        return (yield from deserialize_annotated(hint, context=context))
    elif get_generic_origin(hint) is Literal:
        members = get_generic_args(hint)

        return (yield from deserialize_literal(members))
    elif get_generic_origin(hint) is tuple:
        members = get_generic_args(hint)

        return (yield from deserialize_tuple(members, context=context))
    elif get_generic_origin(hint) is Union:
        members = get_generic_args(hint)

        return (yield from deserialize_union(members, context=context))
    elif isinstance(hint, TypeAliasType):
        return (yield from deserialize(hint.__value__, context=context))
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
        raise TypeError(f"Unsupported type {hint}")
