from typing import Literal

from pydantic import BaseModel


__all__ = (
    "Name",
)


class Name(BaseModel):
    key: Literal["name"] = "name"
    value: str
