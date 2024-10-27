from pydantic import BaseModel

from ....command import Key


__all__ = (
    "Name",
)


class Name(BaseModel):
    key: Key["name"]
    value: str
