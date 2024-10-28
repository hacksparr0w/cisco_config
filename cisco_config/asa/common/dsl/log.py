from typing import Literal, Optional, Union

from pydantic import BaseModel

from ....command import Key


__all__ = (
    "Log",
    "LogInterval",
    "LogOptions"
)


class LogInterval(BaseModel):
    key: Key["interval"]
    seconds: int


class LogOptions(BaseModel):
    level: Optional[int] = None
    interval: Optional[LogInterval] = None


class Log(BaseModel):
    key: Key["log"]
    options: Union[Literal["disable", "default"], LogOptions] = LogOptions()
