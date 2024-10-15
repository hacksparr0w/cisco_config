from typing import Literal

from pydantic import BaseModel


__all__ = (
    "ObjectReference",
)


class ObjectReference(BaseModel):
    key: Literal["object"] = "object"
    name: str
