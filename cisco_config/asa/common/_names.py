from ...command import Command
from ._base import Key


__all__ = (
    "NamesCommand",
)


class NamesCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/n-commands.html#wp4039869163
    """

    key: Key["names"]
