from __future__ import annotations

from typing import (
    Literal,
    Self,
    get_origin as get_generic_origin,
    get_args as get_generic_args
)

from pydantic import BaseModel

from .deserialize import deserialize_model
from .stream import ReplayableIterator
from .token import Token


__all__ = (
    "Command",
    "CommandClassValidationError",
    "Container",
    "MissingCommandNameFieldError",
    "InvalidCommandNameFieldError"
)


class CommandClassValidationError(TypeError):
    pass


class MissingCommandNameFieldError(CommandClassValidationError):
    pass


class InvalidCommandNameFieldError(CommandClassValidationError):
    pass


def _get_command_name(cls: type[Command]) -> str:
    return get_generic_args(cls.__fields__["name"].annotation)[0]


def _validate_command_subclass(cls: type[Command]) -> None:
    field = cls.__fields__.get("name")

    if not field:
        raise MissingCommandNameFieldError

    annotation = field.annotation

    if not get_generic_origin(annotation) is Literal:
        raise InvalidCommandNameFieldError

    args = get_generic_args(field.annotation)

    if len(args) != 1:
        raise InvalidCommandNameFieldError


class Command(BaseModel):
    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        _validate_command_subclass(cls)

    @classmethod
    def get_name(cls) -> str:
        return _get_command_name(cls)

    @classmethod
    def __deserialize__(cls, stream: ReplayableIterator[Token]) -> Self:
        return deserialize_model(cls, stream)


class Container(BaseModel):
    parent: Command
    children: list[Container]
