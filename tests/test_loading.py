import pytest

from cisco_config import Command, loads
from cisco_config.predefined.asa.common.entity import (
    ObjectGroup,
    ObjectGroupType,
    SimpleEntityRegistry
)

from cisco_config.predefined.asa.common.command import (
    DescriptionCommand,
    Eq,
    HostCommand,
    Line,
    Log,
    NetworkObjectCommand,
    ObjectGroupReference,
    Text
)

from cisco_config.predefined.asa.v9_20.command import (
    AccessListRemarkCommand,
    PortfulExtendedAccessListCommand,

    hints as predefined_hints
)


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            "",
            []
        ),
        (
            """
            !
            ! This is a comment
            !
            """,
            []
        ),
        (
            "access-list outside_access_in remark This is a remark",
            [
                AccessListRemarkCommand(
                    name="outside_access_in",
                    remark=Text(content="This is a remark")
                )
            ]
        ),
        (
            """
            access-list outside_access_in remark This is a remark
            access-list outside_access_in line 5 remark This is another remark
            """,
            [
                AccessListRemarkCommand(
                    name="outside_access_in",
                    remark=Text(content="This is a remark")
                ),
                AccessListRemarkCommand(
                    name="outside_access_in",
                    line=Line(number=5),
                    remark=Text(content="This is another remark")
                )
            ]
        ),
        (
            """
            object network HST_192.168.20.148
             host 192.168.20.148
             description VLAN1026_GSNI-FFM-	SDE-IR-10

            object network HST_192.168.20.148
             host 192.168.20.148
             description defrvep01ir10wm
            """,
            [
                NetworkObjectCommand(
                    name="HST_192.168.20.148",
                    target=[HostCommand(value="192.168.20.148")],
                    description=[
                        DescriptionCommand(
                            value=Text(content="VLAN1026_GSNI-FFM- SDE-IR-10")
                        )
                    ]
                ),
                NetworkObjectCommand(
                    name="HST_192.168.20.148",
                    target=[HostCommand(value="192.168.20.148")],
                    description=[
                        DescriptionCommand(
                            value=Text(content="defrvep01ir10wm")
                        )
                    ]
                )
            ]
        )
    ]
)
def test_simple_loading(data: str, expected: list[Command]) -> None:
    assert list(loads(predefined_hints, data)) == expected


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            (
                "access-list MY_ACL extended permit TCP object-group "
                "GRP_NET1691403080 object-group GRP_NET1691403081 "
                "object-group GRP_SVCTCP1652862712 log\n"
                "access-list MY_ACL extended permit UDP object-group "
                "GRP_NET1691403080 object-group GRP_IBMSOBOX eq 888 log"
            ),
            [
                PortfulExtendedAccessListCommand(
                    name="MY_ACL",
                    action="permit",
                    protocol="TCP",
                    source=ObjectGroupReference(name="GRP_NET1691403080"),
                    destination=ObjectGroupReference(
                        name="GRP_NET1691403081"
                    ),
                    destination_port=ObjectGroupReference(
                        name="GRP_SVCTCP1652862712"
                    ),
                    log=Log()
                ),
                PortfulExtendedAccessListCommand(
                    name="MY_ACL",
                    action="permit",
                    protocol="UDP",
                    source=ObjectGroupReference(name="GRP_NET1691403080"),
                    destination=ObjectGroupReference(name="GRP_IBMSOBOX"),
                    destination_port=Eq(value=888),
                    log=Log()
                )
            ]
        )
    ]
)
def test_advanced_loading(data: str, expected: list[Command]) -> None:
    registry = SimpleEntityRegistry(
        object_groups=[
            ObjectGroup(
                name="GRP_NET1691403080",
                type=ObjectGroupType.NETWORK
            ),
            ObjectGroup(
                name="GRP_NET1691403081",
                type=ObjectGroupType.NETWORK
            ),
            ObjectGroup(
                name="GRP_SVCTCP1652862712",
                type=ObjectGroupType.SERVICE
            ),
            ObjectGroup(
                name="GRP_IBMSOBOX",
                type=ObjectGroupType.NETWORK
            )
        ]
    )

    context = {
        "entity_registry": registry
    }

    assert list(loads(predefined_hints, data, context=context)) == expected


@pytest.mark.parametrize(
    "hints, data, expected",
    [
        (
            (),
            "access-list outside_access_in remark This is a remark",
            []
        ),
        (
            (
                AccessListRemarkCommand,
            ),
            """
            clear console-output
            access-list outside_access_in remark This is a remark
            clear console-output
            access-list outside_access_in remark This is another remark
            clear console-output
            """,
            [
                AccessListRemarkCommand(
                    name="outside_access_in",
                    remark=Text(content="This is a remark")
                ),
                AccessListRemarkCommand(
                    name="outside_access_in",
                    remark=Text(content="This is another remark")
                )
            ]
        ),
        (
            (
                NetworkObjectCommand,
            ),
            """
            object network HST_192.168.20.148
             host 192.168.20.148
             description defrvep01ir10wm

            clear console-output

            object network HST_192.168.20.148
             host 192.168.20.148
             clear console-output
             description defrvep01ir10wm

            object network HST_192.168.20.148
             clear console-output
             host 192.168.20.148
             description defrvep01ir10wm

            object network HST_192.168.20.148
             host 192.168.20.148
             description defrvep01ir10wm
            """,
            [
                NetworkObjectCommand(
                    name="HST_192.168.20.148",
                    target=[HostCommand(value="192.168.20.148")],
                    description=[
                        DescriptionCommand(
                            value=Text(content="defrvep01ir10wm")
                        )
                    ]
                ),
                NetworkObjectCommand(
                    name="HST_192.168.20.148",
                    target=[HostCommand(value="192.168.20.148")]
                ),
                NetworkObjectCommand(name="HST_192.168.20.148"),
                NetworkObjectCommand(
                    name="HST_192.168.20.148",
                    target=[HostCommand(value="192.168.20.148")],
                    description=[
                        DescriptionCommand(
                            value=Text(content="defrvep01ir10wm")
                        )
                    ]
                )
            ]
        )
    ]
)
def test_lenient_loading(hints, data, expected) -> None:
    assert list(loads(hints, data, strict=False)) == expected
