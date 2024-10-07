from typing import Literal

from .....command import Command
from ._base import DescriptionCommand
from ._network import HostCommand


__all__ = (
    "NetworkObjectCommand",
)


class NetworkObjectCommand(Command):
    key: Literal["object"] = "object"
    type: Literal["network"] = "network"
    name: str

    target: list[HostCommand] = []
    description: list[DescriptionCommand] = []
