from pydantic import BaseModel

from ....command import Key


__all__ = (
    "User",
)


class User(BaseModel):
    key: Key["user"]
    name: str
