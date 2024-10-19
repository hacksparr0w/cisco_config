from typing import Literal

from pydantic import BaseModel


__all__ = (
    "UserGroupReference",
)


class UserGroupReference(BaseModel):
    key: Literal["user-group"] = "user-group"
    name: str
