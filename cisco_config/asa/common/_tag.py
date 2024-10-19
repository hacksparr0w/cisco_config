from typing import Literal

from pydantic import BaseModel


__all__ = (
    "Tag",
)


class Tag(BaseModel):
    key: Literal["tag"] = "tag"
    value: str
