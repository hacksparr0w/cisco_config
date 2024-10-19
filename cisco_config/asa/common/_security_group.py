from typing import Literal, Union

from pydantic import BaseModel

from ...command import Command


__all__ = (
    "SecurityGroup",
    "SecurityGroupCommand",
    "SecurityGroupName",
    "SecurityGroupReference",
    "SecurityGroupTag"
)


class SecurityGroupTag(BaseModel):
    key: Literal["tag"] = "tag"
    value: str


class SecurityGroupName(BaseModel):
    key: Literal["name"] = "name"
    value: str


class SecurityGroup(BaseModel):
    key: Literal["security-group"] = "security-group"
    target: Union[SecurityGroupName, SecurityGroupTag]


class SecurityGroupCommand(SecurityGroup, Command):
    pass


class SecurityGroupReference(SecurityGroup):
    pass
