from pydantic import BaseModel

from ._base import Key


__all__ = (
    "Level",
)


class Level(BaseModel):
    key: Key["level"]
    value: int
