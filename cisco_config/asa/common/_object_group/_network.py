from typing import Union

from ....command import Command
from .._base import Key
from .._host import Host
from .._object import ObjectReference
from .._subnet import Ipv4Subnet


__all__ = (
    "NetworkObjectGroupCommand",
    "ObjectGroupNetworkObjectCommand",
    "ObjectGroupNetworkObjectModifyCommand",
    "ObjectGroupNetworkObjectRemoveCommand",
    "ObjectGroupNetworkObjectTarget"
)


type ObjectGroupNetworkObjectTarget = Union[
    Host,
    Ipv4Subnet,
    ObjectReference
]


class ObjectGroupNetworkObjectCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/n-commands.html#wp1090353681
    """

    key: Key["network-object"]
    target: ObjectGroupNetworkObjectTarget


class ObjectGroupNetworkObjectRemoveCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/n-commands.html#wp1090353681
    """

    key: Key["no", "network-object"]
    target: ObjectGroupNetworkObjectTarget


ObjectGroupNetworkObjectModifyCommand = Union[
    ObjectGroupNetworkObjectCommand,
    ObjectGroupNetworkObjectRemoveCommand
]


class NetworkObjectGroupCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/o-commands.html#wp4279334402
    """

    key: Key["object-group", "network"]
    name: str
    children: list[ObjectGroupNetworkObjectModifyCommand] = []
