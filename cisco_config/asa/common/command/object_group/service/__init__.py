from typing import Optional, Literal, TypeAlias, Union

from ......command import Command, Key, Subcommand
from . import object


__all__ = (
    "ServiceObjectGroup",
    "ServiceObjectGroupChild"
)


ServiceObjectGroupChild: TypeAlias = Union[
    object.ModifyPortObject,
    object.ModifyServiceObject
]


class ServiceObjectGroup(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/o-commands.html#wp4279334402
    """

    key: Key["object-group", "service"]
    name: str
    protocol: Optional[Literal["tcp", "udp", "tcp-udp"]] = None
    children: Subcommand[ServiceObjectGroupChild]
