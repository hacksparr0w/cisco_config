from typing import Annotated, Literal, Optional, Union

from pydantic.functional_validators import AfterValidator

from ....command import Command
from ..entity import ObjectGroupType, ObjectType
from ._base import Text
from ._host import Host
from ._icmp import IcmpOptions
from ._interface import InterfaceReference
from ._line import Line
from ._log import Log
from ._object_group_reference import (
    NetworkServiceObjectGroupReference,
    ObjectGroupReference,
    SecurityObjectGroupReference,
    validate_object_group_type
)

from ._object_reference import ObjectReference, validate_object_type
from ._security_group import SecurityGroupReference
from ._subnet import IPv4Subnet
from ._time_range import TimeRangeReference
from ._user import User


__all__ = (
    "AccessListIcmpOptions",
    "AccessListRemarkCommand",
    "AccessListSecurityGroup",
    "AccessListTarget",
    "ExtendedIcmpAccessListCommand",
)


type AccessListTarget = Union[
    Host,
    IPv4Subnet,
    Literal["any", "any4", "any6"],
    InterfaceReference,
    Annotated[
        ObjectReference,
        AfterValidator(
            validate_object_type(ObjectType.NETWORK)
        )
    ],
    Annotated[
        ObjectGroupReference,
        AfterValidator(
            validate_object_group_type(ObjectGroupType.NETWORK)
        )
    ],
    NetworkServiceObjectGroupReference
]


type AccessListSecurityGroup = Union[
    SecurityObjectGroupReference,
    SecurityGroupReference
]


type AccessListIcmpOptions = Union[
    IcmpOptions,
    Annotated[
        ObjectGroupReference,
        AfterValidator(
            validate_object_group_type(ObjectGroupType.SERVICE)
        )
    ]
]


class AccessListRemarkCommand(Command):
    key: Literal["access-list"] = "access-list"
    name: str
    line: Optional[Line] = None
    type: Literal["remark"] = "remark"
    value: Text


class ExtendedIcmpAccessListCommand(Command):
    key: Literal["access-list"] = "access-list"
    name: str
    line: Optional[Line] = None
    type: Literal["extended"] = "extended"
    action: Literal["deny", "permit"]
    protocol: Literal["icmp", "icmp6"]
    user: Optional[User] = None
    source_security_group: Optional[AccessListSecurityGroup] = None
    source: AccessListTarget
    destination_security_group: Optional[AccessListSecurityGroup] = None
    destination: AccessListTarget
    options: Optional[AccessListIcmpOptions] = None
    log: Optional[Log] = None
    time: Optional[TimeRangeReference] = None
    inactive: Optional[Literal["inactive"]] = None
