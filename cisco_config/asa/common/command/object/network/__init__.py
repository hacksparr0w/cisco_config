from typing import Union

from ......command import Command, Key, Subcommand
from ... import description
from . import (
    host,
    subnet
)


__all__ = (
    "host",
    "subnet",

    "NetworkObject",
    "NetworkObjectTarget"
)


NetworkObjectTarget = Union[
    host.ModifyHost,
    subnet.ModifySubnet
]


class NetworkObject(Command):
    key: Key["object", "network"]
    name: str

    target: Subcommand[NetworkObjectTarget]
    description: Subcommand[description.ModifyDescription]
