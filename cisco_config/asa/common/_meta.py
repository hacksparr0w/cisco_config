from typing import Literal, Optional

from ...command import Command


__all__ = (
    "AsaVersionCommand",
)


class AsaVersionCommand(Command):
    key: Literal["ASA"] = "ASA"
    type: Literal["Version"] = "Version"
    value: str
    environment: Optional[str] = None
