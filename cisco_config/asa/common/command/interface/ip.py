from ipaddress import IPv4Address as Ipv4Address
from typing import Optional, Union
from typing_extensions import TypeAlias

from .....command import Command, Key
from ... import dsl


__all__ = (
    "IpAddress",
    "ModifyIpAddress",
    "RemoveIpAddress"
)


class IpAddress(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/int-ipu-commands.html#wp1453532950
    """

    key: Key["ip", "address"]
    address: Ipv4Address
    mask: Optional[Ipv4Address] = None
    failover: Optional[dsl.ip.IpAddressFailover] = None


class RemoveIpAddress(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/int-ipu-commands.html#wp1453532950
    """

    key: Key["no", "ip", "address"]
    address: Optional[Ipv4Address] = None


ModifyIpAddress: TypeAlias = Union[
    IpAddress,
    RemoveIpAddress
]
