from typing import Literal, Optional, Union
from typing_extensions import TypeAlias

from pydantic import BaseModel


__all__ = (
    "IcmpOptions",
    "IcmpType"
)


IcmpType: TypeAlias = Union[
    Literal[
        "alternate-address",
        "conversion-error",
        "echo",
        "echo-reply",
        "information-reply",
        "information-request",
        "mask-reply",
        "mask-request",
        "mobile-redirect",
        "parameter-problem",
        "redirect",
        "router-advertisement",
        "router-solicitation",
        "source-quench",
        "time-exceeded",
        "timestamp-reply",
        "timestamp-request",
        "traceroute",
        "unreachable"
    ],
    int
]


class IcmpOptions(BaseModel):
    type: IcmpType
    code: Optional[int] = None
