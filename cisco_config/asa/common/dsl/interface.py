from pydantic import BaseModel

from ....command import Key


__all__ = (
    "Interface",
)


class Interface(BaseModel):
    key: Key["interface"]
    name: str
