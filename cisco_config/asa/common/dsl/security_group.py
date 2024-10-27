from typing import Union

from pydantic import BaseModel

from ....command import Key
from . import name, tag


__all__ = (
    "SecurityGroup",
    "Target"
)


type SecurityGroupTarget = Union[name.Name, tag.Tag]


class SecurityGroup(BaseModel):
    key: Key["security-group"]
    target: SecurityGroupTarget
