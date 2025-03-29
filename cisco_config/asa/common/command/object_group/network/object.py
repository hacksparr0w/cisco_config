from typing import Union
from typing_extensions import TypeAlias

from ......command import Command, Key
from .... import dsl


__all__ = (
    "GroupObject",
    "ModifyGroupObject",
    "ModifyNetworkObject",
    "NetworkObject",
    "NetworkObjectTarget",
    "RemoveGroupObject",
    "RemoveNetworkObject"
)


NetworkObjectTarget: TypeAlias = Union[
    dsl.host.Host,
    dsl.subnet.Ipv4Subnet,
    dsl.object.Object
]


class NetworkObject(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/n-commands.html#wp1090353681
    """

    key: Key["network-object"]
    target: NetworkObjectTarget


class RemoveNetworkObject(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/n-commands.html#wp1090353681
    """

    key: Key["no", "network-object"]
    target: NetworkObjectTarget


class GroupObject(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/A-H/asa-command-ref-A-H/m_g-h.html#wp7992554470
    """

    key: Key["group-object"]
    name: str


class RemoveGroupObject(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/A-H/asa-command-ref-A-H/m_g-h.html#wp7992554470
    """

    key: Key["no", "group-object"]
    name: str


ModifyNetworkObject: TypeAlias = Union[
    GroupObject,
    NetworkObject,
    RemoveGroupObject,
    RemoveNetworkObject
]
