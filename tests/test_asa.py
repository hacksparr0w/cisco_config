import os

from ipaddress import IPv4Address

import cisco_config.asa
import pytest

from cisco_config import Command
from cisco_config.asa.common import (
    AsaVersionCommand,
    BannerCommand,
    DescriptionCommand,
    EnablePasswordCommand,
    FtpModePassiveCommand,
    HostnameCommand,
    InterfaceCommand,
    InterfaceCommandIpAddressCommand,
    InterfaceCommandIpAddressRemoveCommand,
    InterfaceCommandManagementOnlyCommand,
    InterfaceCommandNameCommand,
    InterfaceCommandNameRemoveCommand,
    InterfaceCommandSecurityLevelCommand,
    InterfaceCommandSecurityLevelRemoveCommand,
    InterfaceCommandShutdownCommand,
    InterfaceCommandVlanCommand,
    MacAddressAutoRemoveCommand,
    NamesCommand,
    ObjectNetworkCommand,
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
                MacAddressAutoRemoveCommand(),
                InterfaceCommand(
                   id="GigabitEthernet0/0",
                   name=[
                       InterfaceCommandNameCommand(value="OUTSIDE_VLAN10")
                   ],
                   description=[
                       DescriptionCommand(
                           value=Text(content="to Intrnet")
                        )
                   ],
                   address=[
                       InterfaceCommandIpAddressCommand(
                           address=IPv4Address("172.16.100.1"),
                           mask=IPv4Address("255.255.255.0")
                       )
                   ],
                   shutdown=[
                       InterfaceCommandShutdownCommand()
                   ],
                   security=[
                       InterfaceCommandSecurityLevelCommand(value=0)
                   ]
               ),
                InterfaceCommand(
                     id="GigabitEthernet0/0.35",
                     name=[
                          InterfaceCommandNameCommand(value="OUT")
                     ],
                     address=[
                          InterfaceCommandIpAddressCommand(
                            address=IPv4Address("19.12.76.9"),
                            mask=IPv4Address("255.255.255.240")
                          )
                     ],
                    security=[
                        InterfaceCommandSecurityLevelCommand(value=0)
                    ],
                    vlan=[
                        InterfaceCommandVlanCommand(id=35)
                    ]
                ),
                InterfaceCommand(
                    id="GigabitEthernet0/0.36",
                    name=[
                        InterfaceCommandNameCommand(value="INS")
                    ],
                    description=[
                        DescriptionCommand(
                            value=Text(content="TO Inside networks")
                        )
                    ],
                    address=[
                        InterfaceCommandIpAddressCommand(
                            address=IPv4Address("172.16.10.1"),
                            mask=IPv4Address("255.255.255.0"),
                        )
                    ],
                    security=[
                        InterfaceCommandSecurityLevelCommand(value=100)
                    ],
                    vlan=[
                        InterfaceCommandVlanCommand(id=36)
                    ]
                ),
                InterfaceCommand(
                    id="GigabitEthernet0/1",
                    name=[
                        InterfaceCommandNameCommand(value="DMZ1")
                    ],
                    address=[
                        InterfaceCommandIpAddressCommand(
                            address=IPv4Address("172.16.20.1"),
                            mask=IPv4Address("255.255.252.0"),
                        )
                    ],
                    security=[
                        InterfaceCommandSecurityLevelCommand(value=80)
                    ],
                    shutdown=[
                        InterfaceCommandShutdownCommand()
                    ]
                ),
                InterfaceCommand(
                    id="GigabitEthernet0/2",
                    name=[
                        InterfaceCommandNameRemoveCommand()
                    ],
                    address=[
                        InterfaceCommandIpAddressRemoveCommand()
                    ],
                    security=[
                        InterfaceCommandSecurityLevelRemoveCommand()
                    ],
                    shutdown=[
                        InterfaceCommandShutdownCommand()
                    ]
                ),
                InterfaceCommand(
                    id="GigabitEthernet0/3",
                    name=[
                        InterfaceCommandNameRemoveCommand()
                    ],
                    address=[
                        InterfaceCommandIpAddressRemoveCommand()
                    ],
                    security=[
                        InterfaceCommandSecurityLevelRemoveCommand()
                    ],
                    shutdown=[
                        InterfaceCommandShutdownCommand()
                    ]
                ),
                InterfaceCommand(
                    id="GigabitEthernet0/4",
                    name=[
                        InterfaceCommandNameRemoveCommand()
                    ],
                    address=[
                        InterfaceCommandIpAddressRemoveCommand()
                    ],
                    security=[
                        InterfaceCommandSecurityLevelRemoveCommand()
                    ],
                    shutdown=[
                        InterfaceCommandShutdownCommand()
                    ]
                ),
                InterfaceCommand(
                    id="GigabitEthernet0/5",
                    name=[
                        InterfaceCommandNameRemoveCommand()
                    ],
                    address=[
                        InterfaceCommandIpAddressRemoveCommand()
                    ],
                    security=[
                        InterfaceCommandSecurityLevelRemoveCommand()
                    ],
                    shutdown=[
                        InterfaceCommandShutdownCommand()
                    ]
                ),
                InterfaceCommand(
                    id="GigabitEthernet0/6",
                    name=[
                        InterfaceCommandNameRemoveCommand()
                    ],
                    address=[
                        InterfaceCommandIpAddressRemoveCommand()
                    ],
                    security=[
                        InterfaceCommandSecurityLevelRemoveCommand()
                    ],
                    shutdown=[
                        InterfaceCommandShutdownCommand()
                    ]
                ),
                InterfaceCommand(
                    id="GigabitEthernet0/7",
                    name=[
                        InterfaceCommandNameRemoveCommand()
                    ],
                    address=[
                        InterfaceCommandIpAddressRemoveCommand()
                    ],
                    security=[
                        InterfaceCommandSecurityLevelRemoveCommand()
                    ],
                    shutdown=[
                        InterfaceCommandShutdownCommand()
                    ]
                ),
                InterfaceCommand(
                    id="GigabitEthernet0/8",
                    name=[
                        InterfaceCommandNameRemoveCommand()
                    ],
                    address=[
                        InterfaceCommandIpAddressRemoveCommand()
                    ],
                    security=[
                        InterfaceCommandSecurityLevelRemoveCommand()
                    ],
                    shutdown=[
                        InterfaceCommandShutdownCommand()
                    ]
                ),
                InterfaceCommand(
                    id="Management0/0",
                    name=[
                        InterfaceCommandNameCommand(value="mgmt0")
                    ],
                    address=[
                        InterfaceCommandIpAddressCommand(
                            address=IPv4Address("192.168.10.35"),
                            mask=IPv4Address("255.255.255.0")
                        )
                    ],
                    management=[
                        InterfaceCommandManagementOnlyCommand()
                    ],
                    security=[
                        InterfaceCommandSecurityLevelCommand(value=100)
                    ]
                ),
                BannerCommand(type="login", value=Text(content="")),
                BannerCommand(
                    type="login",
                    value=Text(
                        content=(
                            "************************************************"
                            "*********************"
                        )
                    )
                ),
                BannerCommand(type="login", value=Text(content="Test Inc")),
                BannerCommand(
                    type="login",
                    value=Text(
                        content=(
                            "NOTICE: This system should be used for "
                            "conducting Test Inc"
                        )
                    )
                ),
                BannerCommand(
                    type="login",
                    value=Text(
                        content=(
                            "business or for purposes authorized by Test Inc "
                            "management."
                        )
                    )
                ),
                BannerCommand(
                    type="login",
                    value=Text(
                        content=(
                            "It is mandatory to comply with all the "
                            "requirements listed"
                        )
                    )
                ),
                BannerCommand(
                    type="login",
                    value=Text(
                        content=(
                            "in the applicable security policy and only "
                            "process or"
                        )
                    )
                ),
                BannerCommand(
                    type="login",
                    value=Text(
                        content=(
                            "store the data classes approved for this asset "
                            "type."
                        )
                    )
                ),
                BannerCommand(
                    type="login",
                    value=Text(
                        content=(
                            "Use is subject to audit at any time by Test "
                            "Inc management."
                        )
                    )
                ),
                BannerCommand(
                    type="login",
                    value=Text(
                        content=(
                            "************************************************"
                            "*********************"
                        )
                    )
                ),
                BannerCommand(type="login", value=Text(content="")),
                FtpModePassiveCommand(),
                ObjectNetworkCommand(name="NET_192.168.0.0_16")
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
