from typing import Literal

from pydantic import BaseModel


__all__ = (
    "Line",
)


class Line(BaseModel):
    key: Literal["line"] = "line"
    number: int
