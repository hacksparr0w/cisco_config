from ....command import Command, Key


__all__ = (
    "DisableNames",
    "Names"
)


class Names(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/n-commands.html#wp4039869163
    """

    key: Key["names"]


class DisableNames(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/n-commands.html#wp4039869163
    """

    key: Key["no", "names"]
