from enum import StrEnum
from typing import Literal, Optional, Union

from pydantic import BaseModel

from ...command import Command
from ._icmp import IcmpOptions
from ._object import ObjectReference
from ._operator import Operator


__all__ = (
    "NetworkServiceObjectGroupReference",
    "ObjectGroup",
    "ObjectGroupCommand",
    "ObjectGroupIcmpService",
    "ObjectGroupL4Service",
    "ObjectGroupL4ServiceDestination",
    "ObjectGroupL4ServiceSource",
    "ObjectGroupReference",
    "ObjectGroupSearchCommand",
    "ObjectGroupService",
    "ObjectGroupType",
    "ServiceObjectGroupCommand",
    "ServiceObjectGroupServiceObjectCommand",
    "SecurityObjectGroupReference",
    "UserObjectGroupReference",
)


class ObjectGroupType(StrEnum):
    PROTOCOL = "protocol"
    NETWORK = "network"
    ICMP = "icmp-type"
    SECURITY = "security"
    USER = "user"
    NETWORK_SERVICE = "network-service"
    SERVICE = "service"


class ObjectGroup(BaseModel):
    name: str
    type: ObjectGroupType


class ObjectGroupIcmpService(BaseModel):
    key: Literal["icmp", "icmp6"]
    options: Optional[IcmpOptions] = None


class ObjectGroupL4ServiceSource(BaseModel):
    key: Literal["source"] = "source"
    value: Operator


class ObjectGroupL4ServiceDestination(BaseModel):
    key: Literal["destination"] = "destination"
    value: Operator


class ObjectGroupL4Service(BaseModel):
    protocol: Literal["tcp", "udp", "tcp-udp", "sctp"]
    source: Optional[ObjectGroupL4ServiceSource] = None
    destination: Optional[ObjectGroupL4ServiceDestination] = None


type ObjectGroupService = Union[
    ObjectGroupL4Service,
    ObjectGroupIcmpService,
    ObjectReference,
    str
]


class ObjectGroupSearchCommand(Command):
    no: Optional[Literal["no"]] = None
    key: Literal["object-group-search"] = "object-group-search"
    type: Union[Literal["access-control"], Literal["threshold"]]


class ServiceObjectGroupServiceObjectCommand(Command):
    key: Literal["service-object"] = "service-object"
    service: ObjectGroupService


class ServiceObjectGroupCommand(Command):
    key: tuple[Literal["object-group"], Literal["service"]] = (
        "object-group",
        "service"
    )

    name: str
    protocol: Optional[Literal["tcp", "udp", "tcp-udp"]] = None
    objects: list[ServiceObjectGroupServiceObjectCommand]


ObjectGroupCommand = ServiceObjectGroupCommand


class ObjectGroupReference(BaseModel):
    key: Literal["object-group"] = "object-group"
    name: str


class NetworkServiceObjectGroupReference(BaseModel):
    key: Literal["object-group-network-service"] = \
        "object-group-network-service"

    name: str


class SecurityObjectGroupReference(BaseModel):
    key: Literal["object-group-security"] = "object-group-security"
    name: str


class UserObjectGroupReference(BaseModel):
    key: Literal["object-group-user"] = "object-group-user"
    name: str
