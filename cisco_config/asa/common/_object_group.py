from enum import StrEnum
from typing import Literal, Optional, Union

from pydantic import BaseModel

from ...command import Command
from ._base import Key
from ._icmp import IcmpOptions
from ._object import ObjectReference
from ._operator import Operator


__all__ = (
    "IcmpService",
    "L4Service",
    "L4ServiceDestination",
    "L4ServiceSource",
    "NetworkServiceObjectGroupReference",
    "ObjectGroup",
    "ObjectGroupCommand",
    "ObjectGroupReference",
    "ObjectGroupSearchCommand",
    "ObjectGroupSearchRemoveCommand",
    "ObjectGroupServiceObjectCommand",
    "ObjectGroupServiceObjectModifyCommand",
    "ObjectGroupServiceObjectRemoveCommand",
    "ObjectGroupType",
    "Protocol",
    "SecurityObjectGroupReference",
    "Service",
    "ServiceObjectGroupCommand",
    "UserObjectGroupReference"
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


class IcmpService(BaseModel):
    key: Literal["icmp", "icmp6"]
    options: Optional[IcmpOptions] = None


class L4ServiceSource(BaseModel):
    key: Literal["source"] = "source"
    value: Operator


class L4ServiceDestination(BaseModel):
    key: Literal["destination"] = "destination"
    value: Operator


class L4Service(BaseModel):
    protocol: Literal["tcp", "udp", "tcp-udp", "sctp"]
    source: Optional[L4ServiceSource] = None
    destination: Optional[L4ServiceDestination] = None


type Protocol = str


type Service = Union[
    L4Service,
    IcmpService,
    ObjectReference,
    Protocol
]


class ObjectGroupSearchCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/o-commands.html#wp1852298285
    """

    key: Key["object-group-search"]
    type: Union[Literal["access-control"], Literal["threshold"]]


class ObjectGroupSearchRemoveCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/o-commands.html#wp1852298285
    """

    key: Key["no", "object-group-search"]
    type: Union[Literal["access-control"], Literal["threshold"]]


class ObjectGroupServiceObjectCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/S/asa-command-ref-S/sa-shov-commands.html#wp6965078880
    """

    key: Key["service-object"]
    service: Service


class ObjectGroupServiceObjectRemoveCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/S/asa-command-ref-S/sa-shov-commands.html#wp6965078880
    """

    key: Key["no", "service-object"]
    service: Service


ObjectGroupServiceObjectModifyCommand = Union[
    ObjectGroupServiceObjectCommand,
    ObjectGroupServiceObjectRemoveCommand
]


class ServiceObjectGroupCommand(Command):
    key: Key["object-group", "service"]
    name: str
    protocol: Optional[Literal["tcp", "udp", "tcp-udp"]] = None
    children: list[ObjectGroupServiceObjectModifyCommand] = []


ObjectGroupCommand = ServiceObjectGroupCommand


class ObjectGroupReference(BaseModel):
    key: Key["object-group"]
    name: str


class NetworkServiceObjectGroupReference(BaseModel):
    key: Key["object-group-network-service"]
    name: str


class SecurityObjectGroupReference(BaseModel):
    key: Key["object-group-security"]
    name: str


class UserObjectGroupReference(BaseModel):
    key: Key["object-group-user"]
    name: str
