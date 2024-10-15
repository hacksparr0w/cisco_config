from typing import Literal, Union

from pydantic import BaseModel

from ._object_group_reference import UserObjectGroupReference


__all__ = (
    "User",
    "UserGroupReference",
    "UserReference"
)


class UserGroupReference(BaseModel):
    key: Literal["user-group"] = "user-group"
    name: str


class UserReference(BaseModel):
    key: Literal["user"] = "user"
    name: str


User = Union[
    UserObjectGroupReference,
    UserGroupReference,
    UserReference
]
