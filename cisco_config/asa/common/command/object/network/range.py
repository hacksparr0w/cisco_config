from ipaddress import IPv4Address
from typing import Union
from typing_extensions import TypeAlias

from ......command import Command, Key


__all__ = (
    "ModifyRange",
    "RemoveRange",
    "Range"
)


class Range(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/q-res-commands.html#wp3708965446
    """

    key: Key["range"]
    start: IPv4Address
    end: IPv4Address


class RemoveRange(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/q-res-commands.html#wp3708965446
    """

    key: Key["no", "range"]
    start: IPv4Address
    end: IPv4Address


ModifyRange: TypeAlias = Union[
    Range,
    RemoveRange
]
