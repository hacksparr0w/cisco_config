from typing import Literal, Optional, Union

from pydantic import BaseModel


__all__ = (
    "Log",
    "LogInterval",
    "LogOptions"
)


class LogInterval(BaseModel):
    key: Literal["interval"] = "interval"
    seconds: int


class LogOptions(BaseModel):
    level: Optional[int] = None
    interval: Optional[LogInterval] = None


class Log(BaseModel):
    key: Literal["log"] = "log"
    options: Union[Literal["disable", "default"], LogOptions] = LogOptions()
