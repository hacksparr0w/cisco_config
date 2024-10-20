from pydantic import BaseModel

from ._base import Key, Text


__all__ = (
    "SecondaryVlans",
)


class SecondaryVlans(BaseModel):
    key: Key["secondary"]
    value: Text
