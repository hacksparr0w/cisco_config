from typing import Union
from typing_extensions import TypeAlias

from .....command import Command, Key


__all__ = (
    "ModifySecurityLevel",
    "ResetSecurityLevel",
    "SecurityLevel"
)


class SecurityLevel(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/S/asa-command-ref-S/sa-shov-commands.html#wp2549340847
    """

    key: Key["security-level"]
    value: int


class ResetSecurityLevel(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/S/asa-command-ref-S/sa-shov-commands.html#wp2549340847
    """

    key: Key["no", "security-level"]


ModifySecurityLevel: TypeAlias = Union[
    SecurityLevel,
    ResetSecurityLevel
]
