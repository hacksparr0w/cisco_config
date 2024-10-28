from typing import Annotated, Literal, Optional, Union

from pydantic import AfterValidator

from .....command import Command, Key
from ... import dsl
from ...entity import ObjectGroupType, ObjectType
from ...validation import validate_object_group_types, validate_object_types


__all__ = (
    "AccessList",
    "AccessListPort",
    "AccessListProtocol",
    "AccessListSecurityGroup",
    "AccessListTarget",
    "AccessListUser",
    "ExtendedAccessList",
    "PortboundExtendedAccessList",
    "PortlessExtendedAccessList"
)


type AccessListIcmpOptions = Union[
    dsl.icmp.IcmpOptions,
    Annotated[
        dsl.object_group.ObjectGroup,
        AfterValidator(
            validate_object_group_types(
                ObjectGroupType.SERVICE
            )
        )
    ]
]


type AccessListPort = Union[
    dsl.op.Op,
    Annotated[
        dsl.object_group.ObjectGroup,
        AfterValidator(
            validate_object_group_types(
                ObjectGroupType.SERVICE
            )
        )
    ]
]


type AccessListProtocol = Union[
    Annotated[
        dsl.object_group.ObjectGroup,
        AfterValidator(
            validate_object_group_types(
                ObjectGroupType.PROTOCOL,
                ObjectGroupType.SERVICE
            )
        )
    ],
    Annotated[
        dsl.object.Object,
        AfterValidator(
            validate_object_types(
                ObjectType.SERVICE
            )
        )
    ],
    str
]


type AccessListSecurityGroup = Union[
    dsl.object_group.SecurityObjectGroup,
    dsl.security_group.SecurityGroup
]


type AccessListTarget = Union[
    dsl.host.Host,
    dsl.subnet.Ipv4Subnet,
    Literal["any", "any4", "any6"],
    dsl.interface.Interface,
    Annotated[
        dsl.object.Object,
        AfterValidator(
            validate_object_types(
                ObjectType.NETWORK
            )
        )
    ],
    Annotated[
        dsl.object_group.ObjectGroup,
        AfterValidator(
            validate_object_group_types(
                ObjectGroupType.NETWORK
            )
        )
    ],
    dsl.object_group.NetworkServiceObjectGroup
]


type AccessListUser = Union[
    dsl.object_group.UserObjectGroup,
    dsl.user.User,
    dsl.user_group.UserGroup
]


class IcmpExtendedAccessList(Command):
    key: Key["access-list"]
    name: str
    line: Optional[dsl.line.Line] = None
    type: Key["extended"]
    action: Literal["deny", "permit"]
    protocol: Literal["icmp", "icmp6"]
    user: Optional[AccessListUser] = None
    source_security_group: Optional[AccessListSecurityGroup] = None
    source: AccessListTarget
    destination_security_group: Optional[AccessListSecurityGroup] = None
    destination: AccessListTarget
    options: Optional[AccessListIcmpOptions] = None
    log: Optional[dsl.log.Log] = None
    time_range: Optional[dsl.time_range.TimeRange] = None
    inactive: Optional[Literal["inactive"]] = None


class PortbasedExtendedAccessList(Command):
    key: Key["access-list"]
    name: str
    line: Optional[dsl.line.Line] = None
    type: Key["extended"]
    action: Literal["deny", "permit"]
    protocol: AccessListProtocol
    user: Optional[AccessListUser] = None
    source_security_group: Optional[AccessListSecurityGroup] = None
    source: AccessListTarget
    source_port: Optional[AccessListPort] = None
    destination_security_group: Optional[AccessListSecurityGroup] = None
    destination: AccessListTarget
    destination_port: Optional[AccessListPort] = None
    log: Optional[dsl.log.Log] = None
    time_range: Optional[dsl.time_range.TimeRange] = None
    inactive: Optional[Literal["inactive"]] = None


ExtendedAccessList = Union[
    IcmpExtendedAccessList,
    PortbasedExtendedAccessList
]
