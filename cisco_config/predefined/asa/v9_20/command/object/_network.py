from typing import Literal

from ......command import Command
from ....common.command import DescriptionCommand, HostCommand


__all__ = (
    "NetworkObjectCommand",
)


class NetworkObjectCommand(Command):
    key: Literal["object"] = "object"
    type: Literal["network"] = "network"
    name: str

    target: list[HostCommand]
    description: list[DescriptionCommand]
