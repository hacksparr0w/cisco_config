from pydantic import BaseModel

from ._base import Key


__all__ = (
    "UserGroupReference",
)


class UserGroupReference(BaseModel):
    key: Key["user-group"]
    name: str
