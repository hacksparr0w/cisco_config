from typing import Literal, Optional

from ......command import Command
from ....common.command import Line, Text


__all__ = (
    "AccessListRemarkCommand",
)


class AccessListRemarkCommand(Command):
    key: Literal["access-list"] = "access-list"
    name: str
    line: Optional[Line] = None
    type: Literal["remark"] = "remark"
    remark: Text
