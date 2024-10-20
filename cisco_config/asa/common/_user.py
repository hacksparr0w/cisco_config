from pydantic import BaseModel

from ._base import Key


__all__ = (
    "UserReference",
)


class UserReference(BaseModel):
    key: Key["user"]
    name: str
