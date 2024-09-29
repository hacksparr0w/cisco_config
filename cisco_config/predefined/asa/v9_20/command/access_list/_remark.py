from typing import Literal, Optional

from .....command import Command
from ...common import Text
from ._base import Line


__all__ = (
    "AccessListRemarkCommand",
)


class AccessListRemarkCommand(Command):
    name: Literal["access-list"] = "access-list"
    id: str
    line: Optional[Line] = None
    type: Literal["remark"] = "remark"
    remark: Text
