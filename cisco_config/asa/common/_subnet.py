from ipaddress import IPv4Address
from typing import Literal, Union

from pydantic import BaseModel

from ...command import Command


__all__ = (
    "Ipv4Subnet",
    "SubnetCommand",
    "SubnetModifyCommand",
    "SubnetRemoveCommand"
)


class Ipv4Subnet(BaseModel):
    address: IPv4Address
    mask: IPv4Address


class SubnetCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/S/asa-command-ref-S/su-sz-commands.html#wp2224556864
    """

    key: Literal["subnet"] = "subnet"
    value: Ipv4Subnet


class SubnetRemoveCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/S/asa-command-ref-S/su-sz-commands.html#wp2224556864
    """

    key: tuple[Literal["no"], Literal["subnet"]] = ("no", "subnet")
    value: Ipv4Subnet


SubnetModifyCommand = Union[
    SubnetCommand,
    SubnetRemoveCommand
]
