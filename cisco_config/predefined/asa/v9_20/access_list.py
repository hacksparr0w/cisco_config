from typing import Literal, Optional

from pydantic import BaseModel

from ....command import Command
from ..common import Text


__all__ = (
    "AccessListRemarkCommand",
    "Line",
    "Remark"
)


class Line(BaseModel):
    name: Literal["line"]
    number: int


class Remark(BaseModel):
    name: Literal["remark"]
    text: Text


class AccessListRemarkCommand(Command):
    name: Literal["access-list"]
    id: str
    line: Optional[Line]
    remark: Remark
