from typing import Literal

from ...command import Command
from ._base import Key, Text


__all__ = (
    "BannerCommand",
)


class BannerCommand(Command):
    key: Key["banner"]
    type: Literal["asdm", "exec", "login", "motd"]
    value: Text
