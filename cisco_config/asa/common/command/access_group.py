from typing import Literal, Optional

from ....command import Command, Key
from .. import dsl


__all__ = (
    "AccessGroupInterface",
    "AccessGroupGlobal",
    "RemoveAccessGroupInterface",
    "RemoveAccessGroupGlobal"
)


class AccessGroupGlobal(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/A-H/asa-command-ref-A-H/aa-ac-commands.html#wp3192264241
    """

    key: Key["access-group"]
    name: str
    type: Literal["global"]


class AccessGroupInterface(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/A-H/asa-command-ref-A-H/aa-ac-commands.html#wp3192264241
    """

    key: Key["access-group"]
    name: str
    type: Literal["in", "out"]
    interface: dsl.interface.Interface
    mode: Optional[Literal["per-user-override", "control-plane"]] = None


class RemoveAccessGroupGlobal(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/A-H/asa-command-ref-A-H/aa-ac-commands.html#wp3192264241
    """

    key: Key["no", "access-group"]
    name: str
    type: Literal["global"]


class RemoveAccessGroupInterface(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/A-H/asa-command-ref-A-H/aa-ac-commands.html#wp3192264241
    """

    key: Key["no", "access-group"]
    name: str
    type: Literal["in", "out"]
    interface: dsl.interface.Interface
