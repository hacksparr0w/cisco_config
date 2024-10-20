from pydantic import BaseModel

from ._base import Key


__all__ = (
    "Line",
)


class Line(BaseModel):
    key: Key["line"]
    number: int
