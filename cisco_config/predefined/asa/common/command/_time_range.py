from typing import Literal

from pydantic import BaseModel


__all__ = (
    "TimeRangeReference",
)


class TimeRangeReference(BaseModel):
    key: Literal["time-range"] = "time-range"
    name: str
