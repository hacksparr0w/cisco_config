from pydantic import BaseModel

from ....command import Key
from .text import Text


__all__ = (
    "SecondaryVlan",
)


class SecondaryVlan(BaseModel):
    key: Key["secondary"]
    value: Text
