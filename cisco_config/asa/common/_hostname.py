from typing import Literal

from ...command import Command


__all__ = (
    "HostnameCommand",
)


class HostnameCommand(Command):
    key: Literal["hostname"] = "hostname"
    value: str
