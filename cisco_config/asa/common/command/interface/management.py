from typing import Literal, Optional, Union

from .....command import Command, Key


__all__ = (
    "DisableManagementOnly",
    "ManagementOnly",
    "ModifyManagementOnly",
)


class ManagementOnly(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/m_maa-match-d.html#wp2296849870
    """

    key: Key["management-only"]
    individual: Optional[Literal["individual"]] = None


class DisableManagementOnly(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/m_maa-match-d.html#wp2296849870
    """

    key: Key["no", "management-only"]
    individual: Optional[Literal["individual"]] = None


ModifyManagementOnly = Union[
    DisableManagementOnly,
    ManagementOnly
]
