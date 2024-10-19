from typing import Literal

from ...command import Command

__all__ = (
    "TerminalWidthCommand",
)


class TerminalWidthCommand(Command):
    key: Literal["terminal"] = "terminal"
    type: Literal["width"] = "width"
    value: int
