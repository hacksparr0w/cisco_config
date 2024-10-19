from typing import Literal, Optional

from ...command import Command
from ._interface import InterfaceReference


__all__ = (
    "AccessGroupCommand",
)


class AccessGroupCommand(Command):
    key: Literal["access-group"] = "access-group"
    name: str
    type: Literal["in", "out"]
    interface: InterfaceReference
    mode: Optional[Literal["per-user-override", "control-plane"]] = None
