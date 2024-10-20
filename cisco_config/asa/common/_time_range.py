from pydantic import BaseModel

from ._base import Key


__all__ = (
    "TimeRangeReference",
)


class TimeRangeReference(BaseModel):
    key: Key["time-range"]
    name: str
