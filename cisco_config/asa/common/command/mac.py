from typing import Optional, Union
from typing_extensions import TypeAlias

from ....command import Command, Key
from .. import dsl


__all__ = (
    "AutomaticMacAddress",
    "ModifyAutomaticMacAddress",
    "DisableAutomaticMacAddress"
)


class AutomaticMacAddress(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/m_maa-match-d.html#wp1950933420
    """

    key: Key["mac-address", "auto"]
    prefix: Optional[dsl.mac.MacPrefix] = None


class DisableAutomaticMacAddress(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/m_maa-match-d.html#wp1950933420
    """

    key: Key["no", "mac-address", "auto"]


ModifyAutomaticMacAddress: TypeAlias = Union[
    AutomaticMacAddress,
    DisableAutomaticMacAddress
]
