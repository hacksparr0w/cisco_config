from typing import Union
from typing_extensions import TypeAlias

from ......command import Command, Key, Subcommand
from ... import description
from . import (
    host,
    range,
    subnet
)


__all__ = (
    "host",
    "range",
    "subnet",

    "NetworkObject",
    "NetworkObjectTarget"
)


NetworkObjectTarget: TypeAlias = Union[
    host.ModifyHost,
    range.ModifyRange,
    subnet.ModifySubnet
]


class NetworkObject(Command):
    key: Key["object", "network"]
    name: str

    target: Subcommand[NetworkObjectTarget]
    description: Subcommand[description.ModifyDescription]
