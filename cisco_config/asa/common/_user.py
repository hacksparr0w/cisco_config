from typing import Literal

from pydantic import BaseModel


__all__ = (
    "UserReference",
)


class UserReference(BaseModel):
    key: Literal["user"] = "user"
    name: str
