from ipaddress import IPv4Address
from typing import Annotated, Literal, Optional

from pydantic import BaseModel, AfterValidator

from ...command import Command


__all__ = (
    "InterfaceIpAddressCommand",
    "InterfaceNameCommand",
    "InterfaceReference",
    "InterfaceSecurityLevelCommand",
    "PortChannelInterfaceCommand",
    "StandbyUnit"
)


def _validate_port_channel(value: str) -> str:
    if not value.startswith("Port-channel"):
        raise ValueError

    number = float(value[12:])

    if 1 <= number <= 48:
        return value

    raise ValueError


class InterfaceReference(BaseModel):
    key: Literal["interface"] = "interface"
    name: str


class StandbyUnit(BaseModel):
    key: Literal["standby"] = "standby"
    address: IPv4Address


class InterfaceIpAddressCommand(Command):
    key: tuple[Literal["ip"], Literal["address"]] = ("ip", "address")
    address: IPv4Address
    mask: Optional[IPv4Address] = None
    standby: Optional[StandbyUnit] = None


class InterfaceNameCommand(Command):
    key: Literal["nameif"] = "nameif"
    value: str


class InterfaceSecurityLevelCommand(Command):
    key: Literal["security-level"] = "security-level"
    value: int


class PortChannelInterfaceCommand(Command):
    key: Literal["interface"] = "interface"
    type: Annotated[
        str,
        AfterValidator(
            _validate_port_channel
        )
    ]

    name: list[InterfaceNameCommand] = []
    security: list[InterfaceSecurityLevelCommand] = []
    address: list[InterfaceIpAddressCommand] = []
