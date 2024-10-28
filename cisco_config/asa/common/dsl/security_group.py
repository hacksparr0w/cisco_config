from typing import TypeAlias, Union

from pydantic import BaseModel

from ....command import Key
from . import name, tag


__all__ = (
    "SecurityGroup",
    "Target"
)


SecurityGroupTarget: TypeAlias = Union[name.Name, tag.Tag]


class SecurityGroup(BaseModel):
    key: Key["security-group"]
    target: SecurityGroupTarget
