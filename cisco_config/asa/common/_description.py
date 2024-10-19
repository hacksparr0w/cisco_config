from typing import Literal, Union

from ...command import Command
from ._base import Text


__all__ = (
    "DescriptionCommand",
    "DescriptionModifyCommand",
    "DescriptionRemoveCommand"
)


class DescriptionCommand(Command):
    key: Literal["description"] = "description"
    value: Text


class DescriptionRemoveCommand(Command):
    key: tuple[Literal["no"], Literal["description"]] = ("no", "description")


DescriptionModifyCommand = Union[DescriptionCommand, DescriptionRemoveCommand]
