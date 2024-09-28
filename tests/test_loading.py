import pytest

from cisco_config import Command, loads
from cisco_config.predefined.asa.common import Text
from cisco_config.predefined.asa.v9_20 import (
    AccessListRemarkCommand,

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
    ]
)
def test(data: str, expected: list[Command]):
    assert loads(hints, data) == expected
