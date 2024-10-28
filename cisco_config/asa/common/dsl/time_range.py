from pydantic import BaseModel

from ....command import Key


__all__ = (
    "TimeRange",
)


class TimeRange(BaseModel):
    key: Key["time-range"]
    name: str
