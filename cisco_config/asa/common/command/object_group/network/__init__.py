from ......command import Command, Key, Subcommand
from . import object


__all__ = (
    "object",

    "NetworkObjectGroup"
)


class NetworkObjectGroup(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/o-commands.html#wp4279334402
    """

    key: Key["object-group", "network"]
    name: str
    children: Subcommand[object.ModifyNetworkObject]
