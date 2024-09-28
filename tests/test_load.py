import pytest

from cisco_config import loads
from cisco_config.predefined.asa.v9_20 import AccessListRemarkCommand


def test():
    data = "access-list outside_access_in remark This is a remark"
    command = loads((AccessListRemarkCommand,), data)[0]

    assert isinstance(command, AccessListRemarkCommand)
