from typing import Union
from typing_extensions import TypeAlias

from ......command import Command, Key
from .... import dsl


__all__ = (
    "ModifyPortObject",
    "ModifyServiceObject",
    "PortObject",
    "PortObjectTarget",
    "RemovePortObject",
    "RemoveServiceObject",
    "ServiceObject",
    "ServiceObjectTarget"
)


ServiceObjectTarget: TypeAlias = Union[
    dsl.service.L4Service,
    dsl.service.IcmpService,
    dsl.object.Object,
    str
]


PortObjectTarget: TypeAlias = Union[
    dsl.op.Eq,
    dsl.op.Range
]


class PortObject(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/po-pq-commands.html#wp7375925520
    """

    key: Key["port-object"]
    target: PortObjectTarget


class RemovePortObject(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/I-R/asa-command-ref-I-R/po-pq-commands.html#wp7375925520
    """

    key: Key["no", "port-object"]
    target: PortObjectTarget


ModifyPortObject: TypeAlias = Union[
    PortObject,
    RemovePortObject
]


class ServiceObject(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/S/asa-command-ref-S/sa-shov-commands.html#wp6965078880
    """

    key: Key["service-object"]
    target: ServiceObjectTarget


class RemoveServiceObject(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/S/asa-command-ref-S/sa-shov-commands.html#wp6965078880
    """

    key: Key["no", "service-object"]
    target: ServiceObjectTarget


ModifyServiceObject: TypeAlias = Union[
    ServiceObject,
    RemoveServiceObject
]
