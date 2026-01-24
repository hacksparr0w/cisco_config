from typing import Union
from typing_extensions import TypeAlias

from ......command import Command, Key


__all__ = (
    "ModifyIcmpObject",
    "IcmpObject",
    "RemoveIcmpObject"
)

class GroupObject(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/A-H/asa-command-ref-A-H/m_g-h.html#wp7992554470
    """

    key: Key["group-object"]
    name: str


class RemoveGroupObject(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/A-H/asa-command-ref-A-H/m_g-h.html#wp7992554470
    """

    key: Key["no", "group-object"]
    name: str

class IcmpObject(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/ia-inr-commands.html#wp3763424129
    """

    key: Key["icmp-object"]
    name: str


class RemoveIcmpObject(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/ia-inr-commands.html#wp3763424129
    """

    key: Key["no", "icmp-object"]
    name: str


ModifyIcmpObject: TypeAlias = Union[
    GroupObject,
    RemoveGroupObject,
    IcmpObject,
    RemoveIcmpObject
]
