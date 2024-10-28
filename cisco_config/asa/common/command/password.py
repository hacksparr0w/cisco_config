from typing import Literal, Optional

from ....command import Command, Key
from .. import dsl


__all__ = (
    "EnablePassword",
)


class EnablePassword(Command):
    """
    https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/A-H/asa-command-ref-A-H/e-commands.html#wp3140603370
    """

    key: Key["enable", "password"]
    value: str
    level: Optional[dsl.level.Level] = None
    encryption: Optional[Literal["pbkdf2", "encrypted"]] = None
