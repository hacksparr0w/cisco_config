from ipaddress import IPv4Address
from typing import Literal, Optional, Union

from pydantic import BaseModel

from ...command import Command


__all__ = (
    "ClusterPoolReference",
    "IpAddressCommand",
    "IpAddressFailover",
    "IpAddressModifyCommand",
    "IpAddressRemoveCommand",
    "StandbyIpAddress"
)


class ClusterPoolReference(BaseModel):
    key: Literal["cluster-pool"] = "cluster-pool"
    name: str


class StandbyIpAddress(BaseModel):
    key: Literal["standby"] = "standby"
    address: IPv4Address


IpAddressFailover = Union[
    ClusterPoolReference,
    StandbyIpAddress
]


class IpAddressCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/int-ipu-commands.html#wp1453532950
    """

    key: tuple[Literal["ip"], Literal["address"]] = ("ip", "address")
    address: IPv4Address
    mask: Optional[IPv4Address] = None
    failover: Optional[IpAddressFailover] = None


class IpAddressRemoveCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/int-ipu-commands.html#wp1453532950
    """

    key: tuple[Literal["no"], Literal["ip"], Literal["address"]] = (
        "no",
        "ip",
        "address"
    )

    address: Optional[IPv4Address] = None


IpAddressModifyCommand = Union[
    IpAddressCommand,
    IpAddressRemoveCommand
]
