from typing import Literal, Optional, Union
from typing_extensions import TypeAlias

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
