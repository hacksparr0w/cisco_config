from typing import Optional, Union

from pydantic import BaseModel

from ...command import Command
from ._base import Key
from ._description import DescriptionModifyCommand
from ._ip import IpAddressModifyCommand
from ._management import ManagementOnlyModifyCommand
from ._nameif import NameifModifyCommand
from ._secondary_vlan import SecondaryVlans
from ._security_level import SecurityLevelModifyCommand


__all__ = (
    "InterfaceCommand",
    "InterfaceReference",
    "InterfaceShutdownCommand",
    "InterfaceShutdownModifyCommand",
    "InterfaceShutdownRemoveCommand",
    "InterfaceVlanCommand",
    "InterfaceVlanRemoveCommand",
    "InterfaceVlanModifyCommand"
)


class InterfaceReference(BaseModel):
    key: Key["interface"]
    name: str


class InterfaceShutdownCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/S/asa-command-ref-S/m_shox-sn.html#wp1460040467
    """

    key: Key["shutdown"]


class InterfaceShutdownRemoveCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/S/asa-command-ref-S/m_shox-sn.html#wp1460040467
    """

    key: Key["no", "shutdown"]


InterfaceShutdownModifyCommand = Union[
    InterfaceShutdownCommand,
    InterfaceShutdownRemoveCommand
]


class InterfaceVlanCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/T-Z/asa-command-ref-T-Z/v-commands.html#wp3958987400
    """

    key: Key["vlan"]
    id: int
    secondary: Optional[SecondaryVlans] = None


class InterfaceVlanRemoveCommand(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/T-Z/asa-command-ref-T-Z/v-commands.html#wp3958987400
    """

    key: Key["no", "vlan"]
    id: int
    secondary: Optional[SecondaryVlans] = None


InterfaceVlanModifyCommand = Union[
    InterfaceVlanCommand,
    InterfaceVlanRemoveCommand
]


class InterfaceCommand(Command):
    key: Key["interface"]
    id: str

    name: list[NameifModifyCommand] = []
    description: list[DescriptionModifyCommand] = []
    address: list[IpAddressModifyCommand] = []
    management: list[ManagementOnlyModifyCommand] = []
    security: list[SecurityLevelModifyCommand] = []
    shutdown: list[InterfaceShutdownModifyCommand] = []
    vlan: list[InterfaceVlanModifyCommand] = []
