from typing import Literal, Optional, Union

from pydantic import BaseModel


__all__ = (
    "IcmpType",
    "IcmpOptions"
)


type IcmpType = Union[
    Literal["echo", "echo-reply"],
    int
]


class IcmpOptions(BaseModel):
    type: IcmpType
    code: Optional[int] = None
