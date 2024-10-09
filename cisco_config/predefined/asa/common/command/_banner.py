from typing import Literal, Union

from .....command import Command
from ._base import Text


__all__ = (
    "BannerCommand",
)


class BannerCommand(Command):
    key: Literal["banner"] = "banner"
    type: Literal["asdm", "exec", "login", "motd"]
    value: Text

