from typing import Literal, Optional, Union

from ....command import Command
from .._base import Key
from .._object import ObjectReference
from .._operator import Eq, Range
from .._service import IcmpService, L4Service


__all__ = (
    "ObjectGroupPortObjectCommand",
    "ObjectGroupPortObjectModifyCommand",
    "ObjectGroupPortObjectRemoveCommand",
    "ObjectGroupPortObjectTarget",
    "ObjectGroupServiceObjectCommand",
    "ObjectGroupServiceObjectModifyCommand",
    "ObjectGroupServiceObjectRemoveCommand",
    "ObjectGroupServiceObjectTarget",
    "ServiceObjectGroupCommand",
    "ServiceObjectGroupChildCommand"
)


type ObjectGroupServiceObjectTarget = Union[
    L4Service,
    IcmpService,
    ObjectReference,
    str
]


type ObjectGroupPortObjectTarget = Union[
    Eq,
    Range
]


class ObjectGroupPortObjectCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/po-pq-commands.html#wp7375925520
    """

    key: Key["port-object"]
    target: ObjectGroupPortObjectTarget


class ObjectGroupPortObjectRemoveCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/po-pq-commands.html#wp7375925520
    """

    key: Key["no", "port-object"]
    target: ObjectGroupPortObjectTarget


ObjectGroupPortObjectModifyCommand = Union[
    ObjectGroupPortObjectCommand,
    ObjectGroupPortObjectRemoveCommand
]


class ObjectGroupServiceObjectCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/S/asa-command-ref-S/sa-shov-commands.html#wp6965078880
    """

    key: Key["service-object"]
    target: ObjectGroupServiceObjectTarget


class ObjectGroupServiceObjectRemoveCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/S/asa-command-ref-S/sa-shov-commands.html#wp6965078880
    """

    key: Key["no", "service-object"]
    target: ObjectGroupServiceObjectTarget


ObjectGroupServiceObjectModifyCommand = Union[
    ObjectGroupServiceObjectCommand,
    ObjectGroupServiceObjectRemoveCommand
]


ServiceObjectGroupChildCommand = Union[
    ObjectGroupPortObjectModifyCommand,
    ObjectGroupServiceObjectModifyCommand
]


class ServiceObjectGroupCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/o-commands.html#wp4279334402
    """

    key: Key["object-group", "service"]
    name: str
    protocol: Optional[Literal["tcp", "udp", "tcp-udp"]] = None
    children: list[ServiceObjectGroupChildCommand] = []
