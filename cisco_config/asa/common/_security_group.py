from typing import Literal, Union

from pydantic import BaseModel

from ...command import Command
from ._name import Name
from ._tag import Tag


__all__ = (
    "SecurityGroup",
    "SecurityGroupCommand"
)


class SecurityGroup(BaseModel):
    key: Literal["security-group"] = "security-group"
    name: Union[Name, Tag]


class SecurityGroupCommand(SecurityGroup, Command):
    pass
