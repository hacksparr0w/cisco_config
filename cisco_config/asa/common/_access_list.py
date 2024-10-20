from typing import Annotated, Literal, Optional, Union

from pydantic import BaseModel
from pydantic.functional_validators import AfterValidator

from ...command import Command
from ._base import Text
from ._entity import validate_object_group_type, validate_object_type
from ._host import Host
from ._icmp import IcmpOptions
from ._interface import InterfaceReference
from ._object import ObjectType, ObjectReference
from ._object_group import (
    NetworkServiceObjectGroupReference,
    ObjectGroupType,
    ObjectGroupReference,
    SecurityObjectGroupReference,
    UserObjectGroupReference
)

from ._operator import Operator
from ._security_group import SecurityGroupReference
from ._subnet import IPv4Subnet
from ._time_range import TimeRangeReference
from ._user_group import UserGroupReference
from ._user import UserReference


__all__ = (
    "AccessListIcmpOptions",
    "AccessListLine",
    "AccessListLogInterval",
    "AccessListLogOptions",
    "AccessListLog",
    "AccessListPort",
    "AccessListRemarkCommand",
    "AccessListSecurityGroup",
    "AccessListTarget",
    "AccessListUser",
    "ExtendedIcmpAccessListCommand",
    "ExtendedPortbasedAccessListCommand"
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


type AccessListUser = Union[
    UserObjectGroupReference,
    UserGroupReference,
    UserReference
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


type AccessListPort = Union[
    Operator,
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
    line: Optional[AccessListLine] = None
    type: Literal["remark"] = "remark"
    value: Text


class ExtendedIcmpAccessListCommand(Command):
    key: Literal["access-list"] = "access-list"
    name: str
    line: Optional[AccessListLine] = None
    type: Literal["extended"] = "extended"
    action: Literal["deny", "permit"]
    protocol: Literal["icmp", "icmp6"]
    user: Optional[AccessListUser] = None
    source_security_group: Optional[AccessListSecurityGroup] = None
    source: AccessListTarget
    destination_security_group: Optional[AccessListSecurityGroup] = None
    destination: AccessListTarget
    options: Optional[AccessListIcmpOptions] = None
    log: Optional[AccessListLog] = None
    time: Optional[TimeRangeReference] = None
    inactive: Optional[Literal["inactive"]] = None


class ExtendedPortbasedAccessListCommand(Command):
    key: Literal["access-list"] = "access-list"
    name: str
    line: Optional[AccessListLine] = None
    type: Literal["extended"] = "extended"
    action: Literal["deny", "permit"]
    protocol: Literal["tcp", "udp", "sctp"]
    user: Optional[AccessListUser] = None
    source_security_group: Optional[AccessListSecurityGroup] = None
    source: AccessListTarget
    source_port: Optional[AccessListPort] = None
    destination_security_group: Optional[AccessListSecurityGroup] = None
    destination: AccessListTarget
    destination_port: Optional[AccessListPort] = None
    log: Optional[AccessListLog] = None
    time: Optional[TimeRangeReference] = None
    inactive: Optional[Literal["inactive"]] = None
