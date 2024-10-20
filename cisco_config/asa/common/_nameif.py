from typing import Union

from ...command import Command
from ._base import Key


__all__ = (
    "NameifCommand",
    "NameifRemoveCommand",
    "NameifModifyCommand"
)


class NameifCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/n-commands.html#wp1134161390
    """

    key: Key["nameif"]
    value: str


class NameifRemoveCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/n-commands.html#wp1134161390
    """

    key: Key["no", "nameif"]


NameifModifyCommand = Union[
    NameifCommand,
    NameifRemoveCommand
]
