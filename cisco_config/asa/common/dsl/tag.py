from pydantic import BaseModel

from ....command import Key


__all__ = (
    "Tag",
)


class Tag(BaseModel):
    key: Key["tag"]
    value: str
