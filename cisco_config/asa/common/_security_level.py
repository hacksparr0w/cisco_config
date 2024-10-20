from typing import Union

from ...command import Command
from ._base import Key


__all__ = (
    "SecurityLevelCommand",
    "SecurityLevelModifyCommand",
    "SecurityLevelRemoveCommand"
)


class SecurityLevelCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/S/asa-command-ref-S/sa-shov-commands.html#wp2549340847
    """

    key: Key["security-level"]
    value: int


class SecurityLevelRemoveCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/S/asa-command-ref-S/sa-shov-commands.html#wp2549340847
    """

    key: Key["no", "security-level"]


SecurityLevelModifyCommand = Union[
    SecurityLevelCommand,
    SecurityLevelRemoveCommand
]
