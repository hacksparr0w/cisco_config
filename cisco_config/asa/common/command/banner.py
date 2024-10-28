from typing import Literal

from ....command import Command, Key
from .. import dsl


__all__ = (
    "Banner",
)


class Banner(Command):
    key: Key["banner"]
    type: Literal["asdm", "exec", "login", "motd"]
    value: dsl.text.Text
