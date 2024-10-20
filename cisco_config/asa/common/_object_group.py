from enum import StrEnum
from typing import Literal, Optional, Union

from pydantic import BaseModel

from ...command import Command
from ._base import Key
from ._host import Host
from ._icmp import IcmpOptions
from ._object import ObjectReference
from ._operator import Operator
from ._subnet import Ipv4Subnet


__all__ = (
    "IcmpService",
    "L4Service",
    "L4ServiceDestination",
    "L4ServiceSource",
    "NetworkObjectGroupCommand",
    "NetworkObjectGroupTarget",
    "NetworkServiceObjectGroupReference",
    "ObjectGroup",
    "ObjectGroupCommand",
    "ObjectGroupNetworkObjectCommand",
    "ObjectGroupNetworkObjectModifyCommand",
    "ObjectGroupNetworkObjectRemoveCommand",
    "ObjectGroupProtocolObjectCommand",
    "ObjectGroupProtocolObjectModifyCommand",
    "ObjectGroupProtocolObjectRemoveCommand",
    "ObjectGroupReference",
    "ObjectGroupSearchCommand",
    "ObjectGroupSearchRemoveCommand",
    "ObjectGroupServiceObjectCommand",
    "ObjectGroupServiceObjectModifyCommand",
    "ObjectGroupServiceObjectRemoveCommand",
    "ObjectGroupType",
    "ProtocolObjectGroupCommand",
    "SecurityObjectGroupReference",
    "ServiceObjectGroupCommand",
    "ServiceObjectGroupTarget",
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


type ServiceObjectGroupTarget = Union[
    L4Service,
    IcmpService,
    ObjectReference,
    str
]


type NetworkObjectGroupTarget = Union[
    Host,
    Ipv4Subnet,
    ObjectReference
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


class ObjectGroupNetworkObjectCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/n-commands.html#wp1090353681
    """

    key: Key["network-object"]
    target: NetworkObjectGroupTarget


class ObjectGroupNetworkObjectRemoveCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/n-commands.html#wp1090353681
    """

    key: Key["no", "network-object"]
    target: NetworkObjectGroupTarget


ObjectGroupNetworkObjectModifyCommand = Union[
    ObjectGroupNetworkObjectCommand,
    ObjectGroupNetworkObjectRemoveCommand
]


class ObjectGroupProtocolObjectCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/pr-pz-commands.html#wp2367535905
    """

    key: Key["protocol-object"]
    target: str


class ObjectGroupProtocolObjectRemoveCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/po-pq-commands.html#wp7375925520
    """

    key: Key["no", "protocol-object"]
    target: str


ObjectGroupProtocolObjectModifyCommand = Union[
    ObjectGroupProtocolObjectCommand,
    ObjectGroupProtocolObjectRemoveCommand
]


class ObjectGroupServiceObjectCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/S/asa-command-ref-S/sa-shov-commands.html#wp6965078880
    """

    key: Key["service-object"]
    target: ServiceObjectGroupTarget


class ObjectGroupServiceObjectRemoveCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/S/asa-command-ref-S/sa-shov-commands.html#wp6965078880
    """

    key: Key["no", "service-object"]
    target: ServiceObjectGroupTarget


ObjectGroupServiceObjectModifyCommand = Union[
    ObjectGroupServiceObjectCommand,
    ObjectGroupServiceObjectRemoveCommand
]


class NetworkObjectGroupCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/o-commands.html#wp4279334402
    """

    key: Key["object-group", "network"]
    name: str
    children: list[ObjectGroupNetworkObjectModifyCommand] = []


class ProtocolObjectGroupCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/o-commands.html#wp4279334402
    """

    key: Key["object-group", "protocol"]
    name: str
    children: list[ObjectGroupProtocolObjectModifyCommand] = []


class ServiceObjectGroupCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/o-commands.html#wp4279334402
    """

    key: Key["object-group", "service"]
    name: str
    protocol: Optional[Literal["tcp", "udp", "tcp-udp"]] = None
    children: list[ObjectGroupServiceObjectModifyCommand] = []


ObjectGroupCommand = Union[
    NetworkObjectGroupCommand,
    ServiceObjectGroupCommand
]


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
