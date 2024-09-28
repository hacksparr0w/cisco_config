from typing import Literal, Optional

from pydantic import BaseModel

from ..common import Text
from ....command import Command


__all__ = (
    "AccessListRemarkCommand",
    "Line"
)


class Line(BaseModel):
    name: Literal["line"]
    number: int


class AccessListRemarkCommand(Command):
    name: Literal["access-list"] = "access-list"
    id: str
    line: Optional[Line] = None
    type: Literal["remark"] = "remark"
    remark: Text
