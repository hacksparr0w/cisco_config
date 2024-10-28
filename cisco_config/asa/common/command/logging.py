from ....command import Command, Key


__all__ = (
    "DisableLogging",
    "EnableLogging"
)


class EnableLogging(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/m_log-lz.html#wp2383942576
    """

    key: Key["logging", "enable"]


class DisableLogging(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/m_log-lz.html#wp2383942576
    """

    key: Key["no", "logging", "enable"]
