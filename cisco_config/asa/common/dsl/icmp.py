from typing import Literal, Optional, TypeAlias, Union

from pydantic import BaseModel


__all__ = (
    "IcmpOptions",
    "IcmpType"
)


IcmpType: TypeAlias = Union[
    Literal["echo", "echo-reply"],
    int
]


class IcmpOptions(BaseModel):
    type: IcmpType
    code: Optional[int] = None
