from typing import Literal, Optional, Union

from ...command import Command
from ._base import Key


__all__ = (
    "ManagementOnlyCommand",
    "ManagementOnlyModifyCommand",
    "ManagementOnlyRemoveCommand"
)


class ManagementOnlyCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/m_maa-match-d.html#wp2296849870
    """
    
    key: Key["management-only"]
    individual: Optional[Literal["individual"]] = None


class ManagementOnlyRemoveCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/m_maa-match-d.html#wp2296849870
    """

    key: Key["no", "management-only"]
    individual: Optional[Literal["individual"]] = None


ManagementOnlyModifyCommand = Union[
    ManagementOnlyCommand,
    ManagementOnlyRemoveCommand
]
