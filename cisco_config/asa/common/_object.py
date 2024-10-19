from enum import StrEnum
from typing import Literal, Optional, Union

from pydantic import BaseModel

from ...command import Command
from ._base import Text
from ._host import Host
from ._subnet import IPv4Subnet


__all__ = (
    "NetworkObjectCommand",
    "Object",
    "ObjectCommand",
    "ObjectDescriptionCommand",
    "ObjectHostCommand",
    "ObjectSubnetCommand",
    "ObjectType"
)


class ObjectType(StrEnum):
    NETWORK = "network"
    NETWORK_SERVICE = "network-service"
    SERVICE = "service"


class Object(BaseModel):
    type: ObjectType
    name: str


class ObjectDescriptionCommand(Command):
    key: Literal["description"] = "description"
    value: Text


class ObjectHostCommand(Host, Command):
    pass


class ObjectSubnetCommand(Command):
    key: Literal["subnet"] = "subnet"
    value: IPv4Subnet
    service: Optional[str] = None


class NetworkObjectCommand(Command):
    key: tuple[Literal["object"], Literal["network"]] = ("object", "network")
    name: str

    target: list[Union[ObjectHostCommand, ObjectSubnetCommand]] = []
    description: list[ObjectDescriptionCommand] = []


ObjectCommand = NetworkObjectCommand
