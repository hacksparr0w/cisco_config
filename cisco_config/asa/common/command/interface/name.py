from typing import TypeAlias, Union

from .....command import Command, Key


__all__ = (
    "ModifyName",
    "Name",
    "RemoveName"
)


class Name(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/n-commands.html#wp1134161390
    """

    key: Key["nameif"]
    value: str


class RemoveName(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/n-commands.html#wp1134161390
    """

    key: Key["no", "nameif"]


ModifyName: TypeAlias = Union[
    Name,
    RemoveName
]
