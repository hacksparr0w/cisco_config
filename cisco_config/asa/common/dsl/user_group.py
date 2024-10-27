from pydantic import BaseModel

from ....command import Key


__all__ = (
    "UserGroup",
)


class UserGroup(BaseModel):
    key: Key["user-group"]
    name: str
