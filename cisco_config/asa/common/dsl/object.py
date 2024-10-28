from pydantic import BaseModel

from ....command import Key


__all__ = (
    "Object",
)


class Object(BaseModel):
    key: Key["object"]
    name: str
