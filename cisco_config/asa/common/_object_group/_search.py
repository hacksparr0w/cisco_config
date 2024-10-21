from typing import Literal, Union

from ....command import Command

from .._base import Key


__all__ = (
    "ObjectGroupSearchCommand",
    "ObjectGroupSearchRemoveCommand"
)


class ObjectGroupSearchCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/o-commands.html#wp1852298285
    """

    key: Key["object-group-search"]
    type: Union[Literal["access-control"], Literal["threshold"]]


class ObjectGroupSearchRemoveCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/o-commands.html#wp1852298285
    """

    key: Key["no", "object-group-search"]
    type: Union[Literal["access-control"], Literal["threshold"]]
