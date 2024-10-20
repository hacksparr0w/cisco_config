from typing import Literal, Optional

from pydantic import BaseModel

from ...command import Command
from ._base import Key


__all__ = (
    "AutoMacAddressCommand",
    "AutoMacAddressRemoveCommand",
    "MacAddressPrefix"
)


class MacAddressPrefix(BaseModel):
    key: Literal["prefix"]
    prefix: int


class AutoMacAddressCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/m_maa-match-d.html#wp1950933420
    """

    key: Key["mac-address", "auto"]
    prefix: Optional[MacAddressPrefix] = None


class AutoMacAddressRemoveCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/m_maa-match-d.html#wp1950933420
    """

    key: Key["no", "mac-address", "auto"]
