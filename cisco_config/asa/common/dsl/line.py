from pydantic import BaseModel

from ....command import Key


__all__ = (
    "Line",
)


class Line(BaseModel):
    key: Key["line"]
    number: int
