from typing import Union

from ......command import Command, Key
from .... import dsl


__all__ = (
    "ModifySubnet",
    "RemoveSubnet",
    "Subnet"
)


class Subnet(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/S/asa-command-ref-S/su-sz-commands.html#wp2224556864
    """

    key: Key["subnet"]
    value: dsl.subnet.Ipv4Subnet


class RemoveSubnet(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/S/asa-command-ref-S/su-sz-commands.html#wp2224556864
    """

    key: Key["no", "subnet"]
    value: dsl.subnet.Ipv4Subnet


ModifySubnet = Union[
    RemoveSubnet,
    Subnet
]
