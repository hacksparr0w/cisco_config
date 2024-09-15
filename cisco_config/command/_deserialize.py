from typing import Any

from pydantic import BaseModel

from ..deserialize import DeserializationError
from ..token import Token, Word
from ..stream import ReplayableIterator

from ._base import Command
from ._specification import Specification, Text


__all__ = (
    
)


def deserialize_literal(stream: ReplayableIterator[Token], value: str) -> str:
    token = next(stream)

    if not isinstance(token, Word):
        raise DeserializationError

    if token.value != value:
        raise DeserializationError

    return value


def deserialize_string(stream: ReplayableIterator[Token]) -> str:
    token = next(stream)

    if not isinstance(token, Word):
        raise DeserializationError

    return token.value


def deserialize_integer(stream: ReplayableIterator[Token]) -> int:
    value = _deserialize_string(stream)

    try:
        return int(value)
    except ValueError:
        raise DeserializationError


def deserialize_model(
    stream: ReplayableIterator[Token],
    model: type[BaseModel]
) -> Any:
    pass


def deserialize_command(
    stream: ReplayableIterator[Token],
    specification: Specification
) -> Command:
    pass


def deserialize(stream: ReplayableIterator[Token], hint: Any) -> Any:
    pass
