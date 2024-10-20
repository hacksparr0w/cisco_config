from typing import Literal, Optional

from ...command import Command
from ._base import Key
from ._interface import InterfaceReference


__all__ = (
    "AccessGroupCommand",
    "AccessGroupRemoveCommand"
)


class AccessGroupCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/A-H/asa-command-ref-A-H/aa-ac-commands.html#wp3192264241
    """

    key: Key["access-group"]
    name: str
    type: Literal["in", "out"]
    interface: InterfaceReference
    mode: Optional[Literal["per-user-override", "control-plane"]] = None


class AccessGroupRemoveCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/A-H/asa-command-ref-A-H/aa-ac-commands.html#wp3192264241
    """

    key: Key["access-group"]
    name: str
    type: Literal["in", "out"]
    interface: InterfaceReference
