from enum import StrEnum
from ipaddress import IPv4Address
from typing import Union

from pydantic import BaseModel

from ...command import Command
from ._base import Key
from ._description import DescriptionModifyCommand
from ._subnet import SubnetModifyCommand


__all__ = (
    "NetworkObjectCommand",
    "NetworkObjectHostCommand",
    "NetworkObjectHostModifyCommand",
    "NetworkObjectHostRemoveCommand",
    "NetworkObjectTargetCommand",
    "Object",
    "ObjectCommand",
    "ObjectReference",
    "ObjectType"
)


class ObjectType(StrEnum):
    NETWORK = "network"
    NETWORK_SERVICE = "network-service"
    SERVICE = "service"


class Object(BaseModel):
    type: ObjectType
    name: str


class NetworkObjectHostCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/A-H/asa-command-ref-A-H/m_g-h.html#wp1854487280
    """

    key: Key["host"]
    value: IPv4Address


class NetworkObjectHostRemoveCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/A-H/asa-command-ref-A-H/m_g-h.html#wp1854487280
    """

    key: Key["no", "host"]
    value: IPv4Address


NetworkObjectHostModifyCommand = Union[
    NetworkObjectHostCommand,
    NetworkObjectHostRemoveCommand
]


NetworkObjectTargetCommand = Union[
    SubnetModifyCommand,
    NetworkObjectHostModifyCommand
]


class NetworkObjectCommand(Command):
    key: Key["object", "network"]
    name: str

    target: list[NetworkObjectTargetCommand] = []
    description: list[DescriptionModifyCommand] = []


ObjectCommand = NetworkObjectCommand


class ObjectReference(BaseModel):
    key: Key["object"]
    name: str
