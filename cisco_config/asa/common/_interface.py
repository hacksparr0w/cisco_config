from ipaddress import IPv4Address
from typing import Literal, Optional, Union

from pydantic import BaseModel

from ...command import Command
from ._base import Text
from ._description import DescriptionModifyCommand


__all__ = (
    "InterfaceClusterPool",
    "InterfaceCommand",
    "InterfaceCommandIpAddressCommand",
    "InterfaceCommandIpAddressModifyCommand",
    "InterfaceCommandIpAddressRemoveCommand",
    "InterfaceCommandManagementOnlyCommand",
    "InterfaceCommandManagementOnlyModifyCommand",
    "InterfaceCommandManagementOnlyRemoveCommand",
    "InterfaceCommandNameCommand",
    "InterfaceCommandNameModifyCommand",
    "InterfaceCommandNameRemoveCommand",
    "InterfaceCommandSecurityLevelCommand",
    "InterfaceCommandSecurityLevelModifyCommand",
    "InterfaceCommandSecurityLevelRemoveCommand",
    "InterfaceCommandShutdownCommand",
    "InterfaceCommandShutdownModifyCommand",
    "InterfaceCommandShutdownRemoveCommand",
    "InterfaceCommandVlanCommand",
    "InterfaceCommandVlanModifyCommand",
    "InterfaceCommandVlanRemoveCommand",
    "InterfaceReference",
    "InterfaceSecondaryVlans",
    "InterfaceStandby"
)


class InterfaceReference(BaseModel):
    key: Literal["interface"] = "interface"
    name: str


class InterfaceSecondaryVlans(BaseModel):
    key: Literal["secondary"] = "secondary"
    value: Text


class InterfaceStandby(BaseModel):
    key: Literal["standby"] = "standby"
    address: IPv4Address


class InterfaceClusterPool(BaseModel):
    key: Literal["cluster-pool"] = "cluster-pool"
    name: str


class InterfaceCommandIpAddressCommand(Command):
    key: tuple[Literal["ip"], Literal["address"]] = ("ip", "address")
    address: IPv4Address
    mask: Optional[IPv4Address] = None
    redundancy: Optional[Union[InterfaceStandby, InterfaceClusterPool]] = None


class InterfaceCommandIpAddressRemoveCommand(Command):
    key: tuple[Literal["no"], Literal["ip"], Literal["address"]] = (
        "no",
        "ip",
        "address"
    )

    address: Optional[IPv4Address] = None


InterfaceCommandIpAddressModifyCommand = Union[
    InterfaceCommandIpAddressCommand,
    InterfaceCommandIpAddressRemoveCommand
]


class InterfaceCommandNameCommand(Command):
    key: Literal["nameif"] = "nameif"
    value: str


class InterfaceCommandNameRemoveCommand(Command):
    key: tuple[Literal["no"], Literal["nameif"]] = ("no", "nameif")


InterfaceCommandNameModifyCommand = Union[
    InterfaceCommandNameCommand,
    InterfaceCommandNameRemoveCommand
]


class InterfaceCommandSecurityLevelCommand(Command):
    key: Literal["security-level"] = "security-level"
    value: int


class InterfaceCommandSecurityLevelRemoveCommand(Command):
    key: tuple[Literal["no"], Literal["security-level"]] = (
        "no",
        "security-level"
    )


InterfaceCommandSecurityLevelModifyCommand = Union[
    InterfaceCommandSecurityLevelCommand,
    InterfaceCommandSecurityLevelRemoveCommand
]


class InterfaceCommandShutdownCommand(Command):
    key: Literal["shutdown"] = "shutdown"


class InterfaceCommandShutdownRemoveCommand(Command):
    key: tuple[Literal["no"], Literal["shutdown"]] = ("no", "shutdown")


InterfaceCommandShutdownModifyCommand = Union[
    InterfaceCommandShutdownCommand,
    InterfaceCommandShutdownRemoveCommand
]


class InterfaceCommandVlanCommand(Command):
    key: Literal["vlan"] = "vlan"
    id: int
    secondary: Optional[InterfaceSecondaryVlans] = None


class InterfaceCommandVlanRemoveCommand(Command):
    key: tuple[Literal["no"], Literal["vlan"]] = ("no", "vlan")
    id: int
    secondary: Optional[InterfaceSecondaryVlans] = None


InterfaceCommandVlanModifyCommand = Union[
    InterfaceCommandVlanCommand,
    InterfaceCommandVlanRemoveCommand
]


class InterfaceCommandManagementOnlyCommand(Command):
    key: Literal["management-only"] = "management-only"
    individual: Optional[Literal["individual"]] = None


class InterfaceCommandManagementOnlyRemoveCommand(Command):
    key: tuple[Literal["no"], Literal["management-only"]] = (
        "no",
        "management-only"
    )

    individual: Optional[Literal["individual"]] = None


InterfaceCommandManagementOnlyModifyCommand = Union[
    InterfaceCommandManagementOnlyCommand,
    InterfaceCommandManagementOnlyRemoveCommand
]


class InterfaceCommand(Command):
    key: Literal["interface"] = "interface"
    id: str

    name: list[InterfaceCommandNameModifyCommand] = []
    description: list[DescriptionModifyCommand] = []
    address: list[InterfaceCommandIpAddressModifyCommand] = []
    management: list[InterfaceCommandManagementOnlyModifyCommand] = []
    security: list[InterfaceCommandSecurityLevelModifyCommand] = []
    shutdown: list[InterfaceCommandShutdownModifyCommand] = []
    vlan: list[InterfaceCommandVlanModifyCommand] = []
