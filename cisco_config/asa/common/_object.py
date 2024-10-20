from enum import StrEnum
from ipaddress import IPv4Address
from typing import Literal, Union

from pydantic import BaseModel

from ...command import Command
from ._description import DescriptionModifyCommand
from ._subnet import IPv4Subnet


__all__ = (
    "Object",
    "ObjectCommand",
    "ObjectNetworkCommand",
    "ObjectNetworkCommandHostCommand",
    "ObjectNetworkCommandHostModifyCommand",
    "ObjectNetworkCommandHostRemoveCommand",
    "ObjectNetworkCommandSubnetCommand",
    "ObjectNetworkCommandSubnetModifyCommand",
    "ObjectNetworkCommandSubnetRemoveCommand",
    "ObjectNetworkCommandTargetCommand",
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


class ObjectNetworkCommandSubnetCommand(Command):
    key: Literal["subnet"] = "subnet"
    value: IPv4Subnet


class ObjectNetworkCommandSubnetRemoveCommand(Command):
    key: tuple[Literal["no"], Literal["subnet"]] = ("no", "subnet")
    value: IPv4Subnet


ObjectNetworkCommandSubnetModifyCommand = Union[
    ObjectNetworkCommandSubnetCommand,
    ObjectNetworkCommandSubnetRemoveCommand
]


class ObjectNetworkCommandHostCommand(Command):
    key: Literal["host"] = "host"
    value: IPv4Address


class ObjectNetworkCommandHostRemoveCommand(Command):
    key: tuple[Literal["no"], Literal["host"]] = ("no", "host")
    value: IPv4Address


ObjectNetworkCommandHostModifyCommand = Union[
    ObjectNetworkCommandHostCommand,
    ObjectNetworkCommandHostRemoveCommand
]


ObjectNetworkCommandTargetCommand = Union[
    ObjectNetworkCommandSubnetModifyCommand,
    ObjectNetworkCommandHostModifyCommand
]


class ObjectNetworkCommand(Command):
    key: tuple[Literal["object"], Literal["network"]] = ("object", "network")
    name: str

    target: list[ObjectNetworkCommandTargetCommand] = []
    description: list[DescriptionModifyCommand] = []


ObjectCommand = ObjectNetworkCommand


class ObjectReference(BaseModel):
    key: Literal["object"] = "object"
    name: str
