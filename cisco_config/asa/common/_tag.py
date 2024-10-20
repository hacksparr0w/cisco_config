from pydantic import BaseModel

from ._base import Key


__all__ = (
    "Tag",
)


class Tag(BaseModel):
    key: Key["tag"]
    value: str
