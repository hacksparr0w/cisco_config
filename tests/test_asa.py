import os

from ipaddress import IPv4Address

import cisco_config.asa
import pytest

from cisco_config import Command
from cisco_config.asa.common import (
    AsaVersionCommand,
    AutoMacAddressRemoveCommand,
    DescriptionCommand,
    EnablePasswordCommand,
    HostnameCommand,
    InterfaceCommand,
    InterfaceCommandIpAddressCommand,
    InterfaceCommandNameCommand,
    InterfaceCommandSecurityLevelCommand,
    InterfaceCommandShutdownCommand,
    NamesCommand,
    Text
)


@pytest.mark.parametrize(
    "version, file_name, expected_commands",
    [
        (
            "9.20",
            "./asa.conf",
            [
                AsaVersionCommand(value="9.12(2)"),
                HostnameCommand(value="ASA01"),
                EnablePasswordCommand(value="*****", encryption="pbkdf2"),
                NamesCommand(),
                AutoMacAddressRemoveCommand(),
                InterfaceCommand(
                   id="GigabitEthernet0/0",
                   name=[
                       InterfaceCommandNameCommand(value="OUTSIDE_VLAN10")
                   ],
                   address=[
                       InterfaceCommandIpAddressCommand(
                           address=IPv4Address("172.16.100.1"),
                           mask=IPv4Address("255.255.255.0")
                       )
                   ],
                   description=[
                       DescriptionCommand(value=Text(content="to Intrnet"))
                   ],
                   shutdown=[
                       InterfaceCommandShutdownCommand()
                   ],
                   security=[
                       InterfaceCommandSecurityLevelCommand(value=0)
                   ]
               )
            ]
        ),
    ]
)
def test(
    version: str,
    file_name: str,
    expected_commands: list[Command]
) -> None:
    path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        file_name
    )

    with open(path, "r", encoding="utf-8") as source:
        loaded_commands = cisco_config.asa.load(version, source, strict=False)
        pairs = zip(expected_commands, loaded_commands)

        for expected_command, loaded_command in pairs:
            assert expected_command == loaded_command
