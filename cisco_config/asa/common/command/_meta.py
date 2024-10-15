from typing import Literal

from ....command import Command


__all__ = (
    "AsaVersionCommand",
)


class AsaVersionCommand(Command):
    key: Literal["ASA"] = "ASA"
    type: Literal["Version"] = "Version"
    value: str
    context: Literal["<context>"] = "<context>"
