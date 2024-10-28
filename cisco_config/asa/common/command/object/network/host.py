from ipaddress import IPv4Address as Ipv4Address

from typing import Union
from typing_extensions import TypeAlias

from ......command import Command, Key


__all__ = (
    "Host",
    "ModifyHost",
    "RemoveHost"
)


class Host(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/A-H/asa-command-ref-A-H/m_g-h.html#wp1854487280
    """

    key: Key["host"]
    value: Ipv4Address


class RemoveHost(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/A-H/asa-command-ref-A-H/m_g-h.html#wp1854487280
    """

    key: Key["no", "host"]
    value: Ipv4Address


ModifyHost: TypeAlias = Union[
    Host,
    RemoveHost
]
