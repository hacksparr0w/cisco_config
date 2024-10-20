from pydantic import BaseModel

from ._base import Key


__all__ = (
    "Name",
)


class Name(BaseModel):
    key: Key["name"]
    value: str
