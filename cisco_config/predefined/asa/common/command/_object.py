from typing import Literal

from pydantic import BaseModel


__all__ = (
    "ObjectReference",
)


class ObjectReference(BaseModel):
    anchor: Literal["object"] = "object"
    name: str
