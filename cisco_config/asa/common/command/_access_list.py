from typing import Literal, Optional, Union

from ....command import Command

from ._base import Text
from ._host import Host
from ._line import Line
from ._subnet import IPv4Subnet
from ._user import User


__all__ = (
    "AccessListRemarkCommand",
    "AccessListTarget",
    "ExtendedIcmpAccessListCommand",
)


type AccessListTarget = Union[
    Host,
    IPv4Subnet,
    Literal["any", "any4", "any6"],
]


class AccessListRemarkCommand(Command):
    key: Literal["access-list"] = "access-list"
    name: str
    line: Optional[Line] = None
    type: Literal["remark"] = "remark"
    value: Text


class ExtendedIcmpAccessListCommand(Command):
    key: Literal["access-list"] = "access-list"
    line: Optional[Line] = None
    type: Literal["extended"]
    action: Literal["deny", "permit"]
    protocol: Literal["icmp", "icmp6"]
    user: Optional[User] = None
    source_security_group: Optional[str] = None
    source: AccessListTarget
