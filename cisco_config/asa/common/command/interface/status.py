from typing import Union
from typing_extensions import TypeAlias

from .....command import Command, Key


__all__ = (
    "ModifyStatus",
    "Shutdown",
    "Start"
)


class Shutdown(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/S/asa-command-ref-S/m_shox-sn.html#wp1460040467
    """

    key: Key["shutdown"]


class Start(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/S/asa-command-ref-S/m_shox-sn.html#wp1460040467
    """

    key: Key["no", "shutdown"]


ModifyStatus: TypeAlias = Union[
    Shutdown,
    Start
]
