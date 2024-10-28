from typing import TypeAlias, Union

from ......command import Command, Key


__all__ = (
    "ModifyProtocolObject",
    "ProtocolObject",
    "RemoveProtocolObject"
)


class ProtocolObject(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/pr-pz-commands.html#wp2367535905
    """

    key: Key["protocol-object"]
    target: str


class RemoveProtocolObject(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/po-pq-commands.html#wp7375925520
    """

    key: Key["no", "protocol-object"]
    target: str


ModifyProtocolObject: TypeAlias = Union[
    ProtocolObject,
    RemoveProtocolObject
]
