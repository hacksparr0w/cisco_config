from ....command import Command, Key


__all__ = (
    "DisablePassiveFtpMode",
    "PassiveFtpMode"
)


class PassiveFtpMode(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/A-H/asa-command-ref-A-H/fe-fz-commands.html#wp1203340746
    """

    key: Key["ftp", "mode", "passive"]


class DisablePassiveFtpMode(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/A-H/asa-command-ref-A-H/fe-fz-commands.html#wp1203340746
    """

    key: Key["no", "ftp", "mode", "passive"]
