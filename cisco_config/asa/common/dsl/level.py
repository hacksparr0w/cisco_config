from pydantic import BaseModel

from ....command import Key


__all__ = (
    "Level",
)


class Level(BaseModel):
    key: Key["level"]
    value: int
