from typing import Literal, Optional

from pydantic import BaseModel

from ._interface import InterfaceReference


__all__ = (
    "AccessGroupCommand",
)


class AccessGroupCommand(BaseModel):
    key: Literal["access-group"] = "access-group"
    name: str
    type: Literal["in", "out"]
    interface: InterfaceReference
    mode: Optional[Literal["per-user-override", "control-plane"]] = None
