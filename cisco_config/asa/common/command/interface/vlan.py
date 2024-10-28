from typing import Optional, TypeAlias, Union

from .....command import Command, Key
from ... import dsl


__all__ = (
    "ModifyVlan",
    "RemoveVlan",
    "Vlan"
)


class Vlan(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/T-Z/asa-command-ref-T-Z/v-commands.html#wp3958987400
    """

    key: Key["vlan"]
    id: int
    secondary: Optional[dsl.vlan.SecondaryVlan] = None


class RemoveVlan(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/T-Z/asa-command-ref-T-Z/v-commands.html#wp3958987400
    """

    key: Key["no", "vlan"]
    id: int
    secondary: Optional[dsl.vlan.SecondaryVlan] = None


ModifyVlan: TypeAlias = Union[
    Vlan,
    RemoveVlan
]
