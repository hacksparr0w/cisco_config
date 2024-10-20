from typing import Optional

from ...command import Command
from ._base import Key


__all__ = (
    "HostnameCommand",
    "HostnameRemoveCommand"
)


class HostnameCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/A-H/asa-command-ref-A-H/m_g-h.html#wp3854927134
    """

    key: Key["hostname"]
    value: str


class HostnameRemoveCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/A-H/asa-command-ref-A-H/m_g-h.html#wp3854927134
    """

    key: Key["no", "hostname"]
    value: Optional[str] = None
