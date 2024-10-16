from typing import Literal, Union

from pydantic import BaseModel

from ._object_group_reference import UserObjectGroupReference
from ._user_group import UserGroupReference


__all__ = (
    "User",
    "UserReference"
)


class UserReference(BaseModel):
    key: Literal["user"] = "user"
    name: str


type User = Union[
    UserObjectGroupReference,
    UserGroupReference,
    UserReference
]
