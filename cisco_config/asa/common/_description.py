from typing import Union

from ...command import Command
from ._base import Key, Text


__all__ = (
    "DescriptionCommand",
    "DescriptionModifyCommand",
    "DescriptionRemoveCommand"
)


class DescriptionCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/A-H/asa-command-ref-A-H/m_da-dg.html#wp4232208511
    """

    key: Key["description"]
    value: Text


class DescriptionRemoveCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/A-H/asa-command-ref-A-H/m_da-dg.html#wp4232208511
    """

    key: Key["no", "description"]


DescriptionModifyCommand = Union[DescriptionCommand, DescriptionRemoveCommand]
