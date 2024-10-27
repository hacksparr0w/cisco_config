from typing import Optional

from ....command import Command, Key


__all__ = (
    "DomainName",
    "RemoveDomainName"
)


class DomainName(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/A-H/asa-command-ref-A-H/m_dn-dz.html#wp3961200795
    """

    key: Key["domain-name"]
    value: str


class RemoveDomainName(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/A-H/asa-command-ref-A-H/m_dn-dz.html#wp3961200795
    """

    key: Key["no", "domain-name"]
    value: Optional[str] = None
