import os

from ipaddress import IPv4Address as Ipv4Address

import cisco_config.asa
import pytest

from cisco_config import Command
from cisco_config.asa.common import (
    AsaVersionCommand,
    AutoMacAddressRemoveCommand,
    BannerCommand,
    DescriptionCommand,
    EnablePasswordCommand,
    HostnameCommand,
    InterfaceCommand,
    InterfaceShutdownCommand,
    InterfaceVlanCommand,
    IpAddressCommand,
    IpAddressRemoveCommand,
    Ipv4Subnet,
    ManagementOnlyCommand,
    NameifCommand,
    NameifRemoveCommand,
    NamesCommand,
    NetworkObjectCommand,
    PassiveFtpModeCommand,
    SecurityLevelCommand,
    SecurityLevelRemoveCommand,
    SubnetCommand,
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
                    name=[NameifCommand(value="OUTSIDE_VLAN10")],
                    description=[
                        DescriptionCommand(value=Text(content="to Intrnet"))
                    ],
                    address=[
                        IpAddressCommand(
                           address=Ipv4Address("172.16.100.1"),
                           mask=Ipv4Address("255.255.255.0")
                       )
                   ],
                   shutdown=[InterfaceShutdownCommand()],
                   security=[SecurityLevelCommand(value=0)]
                ),
                InterfaceCommand(
                    id="GigabitEthernet0/0.35",
                    name=[NameifCommand(value="OUT")],
                    address=[
                        IpAddressCommand(
                            address=Ipv4Address("19.12.76.9"),
                            mask=Ipv4Address("255.255.255.240")
                        )
                    ],
                    security=[SecurityLevelCommand(value=0)],
                    vlan=[
                        InterfaceVlanCommand(id=35)
                    ]
                ),
                InterfaceCommand(
                    id="GigabitEthernet0/0.36",
                    name=[NameifCommand(value="INS")],
                    description=[
                        DescriptionCommand(
                            value=Text(content="TO Inside networks")
                        )
                    ],
                    address=[
                        IpAddressCommand(
                            address=Ipv4Address("172.16.10.1"),
                            mask=Ipv4Address("255.255.255.0")
                        )
                    ],
                    security=[SecurityLevelCommand(value=100)],
                    vlan=[InterfaceVlanCommand(id=36)]
                ),
                InterfaceCommand(
                    id="GigabitEthernet0/1",
                    name=[NameifCommand(value="DMZ1")],
                    address=[
                        IpAddressCommand(
                            address=Ipv4Address("172.16.20.1"),
                            mask=Ipv4Address("255.255.252.0"),
                        )
                    ],
                    security=[SecurityLevelCommand(value=80)],
                    shutdown=[InterfaceShutdownCommand()]
                ),
                InterfaceCommand(
                    id="GigabitEthernet0/2",
                    name=[NameifRemoveCommand()],
                    address=[IpAddressRemoveCommand()],
                    security=[SecurityLevelRemoveCommand()],
                    shutdown=[InterfaceShutdownCommand()]
                ),
                InterfaceCommand(
                    id="GigabitEthernet0/3",
                    name=[NameifRemoveCommand()],
                    address=[IpAddressRemoveCommand()],
                    security=[SecurityLevelRemoveCommand()],
                    shutdown=[InterfaceShutdownCommand()]
                ),
                InterfaceCommand(
                    id="GigabitEthernet0/4",
                    name=[NameifRemoveCommand()],
                    address=[IpAddressRemoveCommand()],
                    security=[SecurityLevelRemoveCommand()],
                    shutdown=[InterfaceShutdownCommand()]
                ),
                InterfaceCommand(
                    id="GigabitEthernet0/5",
                    name=[NameifRemoveCommand()],
                    address=[IpAddressRemoveCommand()],
                    security=[SecurityLevelRemoveCommand()],
                    shutdown=[InterfaceShutdownCommand()]
                ),
                InterfaceCommand(
                    id="GigabitEthernet0/6",
                    name=[NameifRemoveCommand()],
                    address=[IpAddressRemoveCommand()],
                    security=[SecurityLevelRemoveCommand()],
                    shutdown=[InterfaceShutdownCommand()]
                ),
                InterfaceCommand(
                    id="GigabitEthernet0/7",
                    name=[NameifRemoveCommand()],
                    address=[IpAddressRemoveCommand()],
                    security=[SecurityLevelRemoveCommand()],
                    shutdown=[InterfaceShutdownCommand()]
                ),
                InterfaceCommand(
                    id="GigabitEthernet0/8",
                    name=[NameifRemoveCommand()],
                    address=[IpAddressRemoveCommand()],
                    security=[SecurityLevelRemoveCommand()],
                    shutdown=[InterfaceShutdownCommand()]
                ),
                InterfaceCommand(
                    id="Management0/0",
                    name=[NameifCommand(value="mgmt0")],
                    address=[
                        IpAddressCommand(
                            address=Ipv4Address("192.168.10.35"),
                            mask=Ipv4Address("255.255.255.0")
                        )
                    ],
                    management=[ManagementOnlyCommand()],
                    security=[SecurityLevelCommand(value=100)]
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
                PassiveFtpModeCommand(),
                NetworkObjectCommand(name="NET_192.168.0.0_16"),
                NetworkObjectCommand(
                    name="NET_192.169.0.0_16",
                    target=[
                        SubnetCommand(
                            value=Ipv4Subnet(
                                address=Ipv4Address("192.169.0.0"),
                                mask=Ipv4Address("255.255.0.0")
                            )
                        )
                    ]
                ),
                NetworkObjectCommand(
                    name="NET_192.170.0.0_16",
                    target=[
                        SubnetCommand(
                            value=Ipv4Subnet(
                                address=Ipv4Address("192.170.0.0"),
                                mask=Ipv4Address("255.255.0.0")
                            )
                        )
                    ]
                ),
                NetworkObjectCommand(
                    name="NET_192.171.0.0_16",
                    target=[
                        SubnetCommand(
                            value=Ipv4Subnet(
                                address=Ipv4Address("192.171.0.0"),
                                mask=Ipv4Address("255.255.0.0")
                            )
                        )
                    ]
                ),
                NetworkObjectCommand(
                    name="NET_192.172.0.0_16",
                    target=[
                        SubnetCommand(
                            value=Ipv4Subnet(
                                address=Ipv4Address("192.172.0.0"),
                                mask=Ipv4Address("255.255.0.0")
                            )
                        )
                    ]
                ),
                NetworkObjectCommand(
                    name="NET_192.173.0.0_16",
                    target=[
                        SubnetCommand(
                            value=Ipv4Subnet(
                                address=Ipv4Address("192.173.0.0"),
                                mask=Ipv4Address("255.255.0.0")
                            )
                        )
                    ]
                ),
                NetworkObjectCommand(
                    name="NET_Testing01",
                    target=[
                        SubnetCommand(
                            value=Ipv4Subnet(
                                address=Ipv4Address("192.174.0.0"),
                                mask=Ipv4Address("255.255.0.0")
                            )
                        )
                    ]
                ),
                NetworkObjectCommand(
                    name="NET_ThisIsReal_Network_For_VS",
                    target=[
                        SubnetCommand(
                            value=Ipv4Subnet(
                                address=Ipv4Address("192.175.0.0"),
                                mask=Ipv4Address("255.255.0.0")
                            )
                        )
                    ]
                ),
                NetworkObjectCommand(
                    name="NET_192.176.0.0_16",
                    target=[
                        SubnetCommand(
                            value=Ipv4Subnet(
                                address=Ipv4Address("192.176.0.0"),
                                mask=Ipv4Address("255.255.0.0")
                            )
                        )
                    ]
                ),
                NetworkObjectCommand(
                    name="NET_192.177.0.0_16",
                    target=[
                        SubnetCommand(
                            value=Ipv4Subnet(
                                address=Ipv4Address("192.177.0.0"),
                                mask=Ipv4Address("255.255.0.0")
                            )
                        )
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
