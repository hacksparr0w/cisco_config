from typing import Optional

from .....command import Command, Key
from ... import dsl


__all__ = (
    "AccessListRemark",
)


class AccessListRemark(Command):
    key: Key["access-list"]
    name: str
    line: Optional[dsl.line.Line] = None
    type: Key["remark"]
    value: dsl.text.Text
