from typing import Literal, Optional

from ....command import Command, Key


__all__ = (
    "PagerLines",
)


class PagerLines(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/pa-pn-commands.html#wp4583104900
    """

    key: Key["pager"]
    type: Optional[Literal["lines"]] = "lines"
    value: int
