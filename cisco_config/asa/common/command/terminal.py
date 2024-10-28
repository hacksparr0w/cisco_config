from ....command import Command, Key


__all__ = (
    "ResetTerminalWidth",
    "TerminalWidth"
)


class TerminalWidth(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/T-Z/asa-command-ref-T-Z/m_ta-tk.html#wp4037792375
    """

    key: Key["terminal", "width"]
    value: int


class ResetTerminalWidth(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/T-Z/asa-command-ref-T-Z/m_ta-tk.html#wp4037792375
    """

    key: Key["no", "terminal", "width"]
    value: int
