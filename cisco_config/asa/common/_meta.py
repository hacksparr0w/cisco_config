from typing import Literal, Optional

from ...command import Command
from ._base import Key


__all__ = (
    "AsaVersionCommand",
)


class AsaVersionCommand(Command):
    key: Key["ASA"]
    type: Literal["Version"] = "Version"
    value: str
    environment: Optional[str] = None
