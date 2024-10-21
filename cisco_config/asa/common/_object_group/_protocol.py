from typing import Union

from ....command import Command
from .._base import Key


__all__ = (
    "ObjectGroupProtocolObjectCommand",
    "ObjectGroupProtocolObjectModifyCommand",
    "ObjectGroupProtocolObjectRemoveCommand",
    "ProtocolObjectGroupCommand"
)


class ObjectGroupProtocolObjectCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/pr-pz-commands.html#wp2367535905
    """

    key: Key["protocol-object"]
    target: str


class ObjectGroupProtocolObjectRemoveCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/po-pq-commands.html#wp7375925520
    """

    key: Key["no", "protocol-object"]
    target: str


ObjectGroupProtocolObjectModifyCommand = Union[
    ObjectGroupProtocolObjectCommand,
    ObjectGroupProtocolObjectRemoveCommand
]


class ProtocolObjectGroupCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/o-commands.html#wp4279334402
    """

    key: Key["object-group", "protocol"]
    name: str
    children: list[ObjectGroupProtocolObjectModifyCommand] = []
