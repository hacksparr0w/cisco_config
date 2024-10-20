from typing import Optional

from ...command import Command
from ._base import Key


__all__ = (
    "DomainNameCommand",
    "DomainNameRemoveCommand"
)


class DomainNameCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/A-H/asa-command-ref-A-H/m_dn-dz.html#wp3961200795
    """

    key: Key["domain-name"]
    value: str


class DomainNameRemoveCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/A-H/asa-command-ref-A-H/m_dn-dz.html#wp3961200795
    """

    key: Key["no", "domain-name"]
    value: Optional[str] = None
