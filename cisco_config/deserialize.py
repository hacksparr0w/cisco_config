from typing import (
    Any,
    Literal,
    Protocol,
    Self,
    Union,

    get_origin as get_generic_origin,
    get_args as get_generic_args,
    runtime_checkable
)

from pydantic import BaseModel

from .stream import ReplayableIterator
from .token import Token, Word


__all__ = (
    "Deserializable",
    "DeserializationError"
)


@runtime_checkable
class Deserializable(Protocol):
    @classmethod
    def __deserialize__(cls, stream: ReplayableIterator[Token]) -> Self:
        ...


class DeserializationError(Exception):
    pass


def deserialize_deserializable(
    stream: ReplayableIterator[Token],
    deserializable: type[Deserializable]
) -> Any:
    return deserializable.__deserialize__(stream)


def deserialize_string(stream: ReplayableIterator[Token]) -> str:
    token = next(stream)

    if not isinstance(token, Word):
        raise DeserializationError

    return token.value


def deserialize_integer(stream: ReplayableIterator[Token]) -> int:
    value = deserialize_string(stream)

    try:
        return int(value)
    except ValueError:
        raise DeserializationError


def deserialize_literal(stream: ReplayableIterator[Token], hint: Any) -> str:
    value = get_generic_args(hint)[0]
    string = deserialize_string(stream)

    if string != value:
        raise DeserializationError

    return string


def deserialize_model(
    stream: ReplayableIterator[Token],
    model: type[BaseModel]
) -> Any:
    properties = {}

    for key, field in model.__fields__.items():
        value = deserialize(stream, field.annotation)

        properties[key] = value

    return model.model_validate(properties)


def deserialize_none(stream: ReplayableIterator[Token]) -> None:
    return None


def deserialize_union(stream: ReplayableIterator[Token], hint: Any) -> Any:
    for argument in get_generic_args(hint):
        record = stream.start_recording()

        try:
            return deserialize(stream, argument)
        except DeserializationError:
            if stream.has_recorded(record):
                stream.replay(record)

    raise DeserializationError


def deserialize(stream: ReplayableIterator[Token], hint: Any) -> Any:
    if hint is type(None):
        return deserialize_none(stream)
    elif hint is str:
        return deserialize_string(stream)
    elif hint is int:
        return deserialize_integer(stream)
    elif isinstance(hint, Deserializable):
        return deserialize_deserializable(stream, hint)
    elif issubclass(hint, BaseModel):
        return deserialize_model(stream, hint)
    elif get_generic_origin(hint) is Literal:
        return deserialize_literal(stream, hint)
    elif get_generic_origin(hint) is Union:
        return deserialize_union(stream, hint)
    else:
        raise NotImplementedError
