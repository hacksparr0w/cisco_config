from typing import Literal, Union

from .....command import Command
from ._base import DescriptionCommand
from ._network import HostCommand, SubnetCommand


__all__ = (
    "NetworkObjectCommand",
)


class NetworkObjectCommand(Command):
    key: Literal["object"] = "object"
    type: Literal["network"] = "network"
    name: str

    target: list[Union[HostCommand, SubnetCommand]] = []
    description: list[DescriptionCommand] = []
