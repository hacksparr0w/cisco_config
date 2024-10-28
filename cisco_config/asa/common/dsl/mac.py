from pydantic import BaseModel

from ....command import Key


__all__ = (
    "MacPrefix",
)


class MacPrefix(BaseModel):
    key: Key["prefix"]
    prefix: int
