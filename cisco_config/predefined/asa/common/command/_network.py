from ipaddress import IPv4Address
from typing import Annotated, Literal, Optional, Union

from pydantic import BaseModel, AfterValidator

from .....command import Command
from ..entity import ObjectGroupType
from ._object_reference import ObjectReference
from ._object_group_reference import (
    ObjectGroupReference,
    NetworkServiceObjectGroupReference,
    validate_object_group_type
)

from ._op import Op


__all__ = (
    "Host",
    "HostCommand",
    "IPv4Subnet",
    "Network",
    "NetworkInterfaceReference",
    "Port",
    "SubnetCommand"
)


class Host(BaseModel):
    key: Literal["host"] = "host"
    value: str


class HostCommand(Host, Command):
    pass


class IPv4Subnet(BaseModel):
    address: IPv4Address
    mask: IPv4Address


class NetworkInterfaceReference(BaseModel):
    key: Literal["interface"] = "interface"
    name: str


class SubnetCommand(Command):
    key: Literal["subnet"] = "subnet"
    value: IPv4Subnet
    service: Optional[str] = None


Network = Union[
    Literal["any", "any4", "any6"],
    Host,
    NetworkInterfaceReference,
    ObjectReference,
    ObjectGroupReference,
    NetworkServiceObjectGroupReference,
    IPv4Subnet
]


Port = Union[
    Annotated[
        ObjectGroupReference,
        AfterValidator(
            validate_object_group_type(ObjectGroupType.SERVICE)
        )
    ],
    Op
]
