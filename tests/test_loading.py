from textwrap import dedent

import pytest

from cisco_config import Command, loads
from cisco_config.predefined.asa.common import Text
from cisco_config.predefined.asa.v9_20 import (
    AccessListRemarkCommand,
    Line,
    Log,
    LogSpecification,
    ObjectGroupReference,
    PortfulExtendedAccessListCommand,

    hints
)


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            "access-list outside_access_in remark This is a remark",
            [
                AccessListRemarkCommand(
                    id="outside_access_in",
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
                    id="outside_access_in",
                    remark=Text(content="This is a remark")
                ),
                AccessListRemarkCommand(
                    id="outside_access_in",
                    line=Line(number=5),
                    remark=Text(content="This is another remark")
                )
            ]
        ),
        (
            "access-list MY_ACL extended permit TCP object-group GRP_NET1691403080 object-group GRP_NET1691403081 object-group GRP_SVCTCP1652862712 log",
            [
                PortfulExtendedAccessListCommand(
                    id="MY_ACL",
                    action="permit",
                    protocol="TCP",
                    source=ObjectGroupReference(id="GRP_NET1691403080"),
                    source_port=ObjectGroupReference(id="GRP_NET1691403081"),
                    destination=ObjectGroupReference(id="GRP_SVCTCP1652862712"),
                    log=Log()
                )
            ]
        )
    ]
)
def test(data: str, expected: list[Command]):
    assert loads(hints, data) == expected
