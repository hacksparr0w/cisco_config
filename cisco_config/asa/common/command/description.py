from typing import Union

from ....command import Command, Key
from .. import dsl


__all__ = (
    "Description",
    "ModifyDescription",
    "RemoveDescription"
)


class Description(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/A-H/asa-command-ref-A-H/m_da-dg.html#wp4232208511
    """

    key: Key["description"]
    value: dsl.text.Text


class RemoveDescription(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/A-H/asa-command-ref-A-H/m_da-dg.html#wp4232208511
    """

    key: Key["no", "description"]


ModifyDescription = Union[Description, RemoveDescription]
