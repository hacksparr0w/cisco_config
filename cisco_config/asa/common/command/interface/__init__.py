from .....command import Command, Key, Subcommand

from .. import description
from . import (
    ip,
    management,
    name,
    security,
    status,
    vlan
)


__all__ = (
    "ip",
    "management",
    "name",
    "security",
    "status",
    "vlan",

    "Interface"
)


class Interface(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/int-ipu-commands.html#wp5150130770
    """

    key: Key["interface"]
    id: str

    name: Subcommand[name.ModifyName]
    description: Subcommand[description.ModifyDescription]
    address: Subcommand[ip.ModifyIpAddress]
    management: Subcommand[management.ModifyManagementOnly]
    security: Subcommand[security.ModifySecurityLevel]
    status: Subcommand[status.ModifyStatus]
    vlan: Subcommand[vlan.ModifyVlan]
