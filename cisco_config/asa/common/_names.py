from typing import Literal

from ...command import Command


__all__ = (
    "NamesCommand",
)


class NamesCommand(Command):
    key: Literal["names"] = "names"
