from typing import Union

from pydantic import BaseModel

from ...command import Command
from ._base import Key
from ._name import Name
from ._tag import Tag


__all__ = (
    "SecurityGroupCommand",
    "SecurityGroupReference",
    "SecurityGroupRemoveCommand",
    "SecurityGroupTarget"
)


type SecurityGroupTarget = Union[Name, Tag]


class SecurityGroupReference(BaseModel):
    key: Key["security-group"]
    target: SecurityGroupTarget


class SecurityGroupCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/S/asa-command-ref-S/sa-shov-commands.html#wp2301402396
    """

    key: Key["security-group"]
    target: SecurityGroupTarget


class SecurityGroupRemoveCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/S/asa-command-ref-S/sa-shov-commands.html#wp2301402396
    """

    key: Key["no", "security-group"]
    target: SecurityGroupTarget
