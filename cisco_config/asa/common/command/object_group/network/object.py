from typing import TypeAlias, Union

from ......command import Command, Key
from .... import dsl


__all__ = (
    "ModifyNetworkObject",
    "NetworkObject",
    "NetworkObjectTarget",
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


ModifyNetworkObject: TypeAlias = Union[
    NetworkObject,
    RemoveNetworkObject
]
