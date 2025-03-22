from ......command import Command, Key, Subcommand
from ... import description
from . import service


__all__ = (
    "service",

    "ServiceObject"
)


class ServiceObject(Command):
    """
    https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/S/asa-command-ref-S/sa-shov-commands.html#wp3114971809
    """

    key: Key["object", "service"]
    name: str

    target: Subcommand[service.Service]
    description: Subcommand[description.ModifyDescription]
