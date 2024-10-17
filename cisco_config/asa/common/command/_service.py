from typing import Literal, Optional, Union

from pydantic import BaseModel

from ._icmp import IcmpOptions
from ._op import Op
from ._object_reference import ObjectReference


__all__ = (
    "IcmpService",
    "L4ServiceSource",
    "L4ServiceDestination",
    "L4Service",
    "Protocol",
    "Service"
)


class IcmpService(BaseModel):
    key: Literal["icmp", "icmp6"]
    options: Optional[IcmpOptions] = None


class L4ServiceSource(BaseModel):
    key: Literal["source"] = "source"
    value: Op


class L4ServiceDestination(BaseModel):
    key: Literal["destination"] = "destination"
    value: Op


class L4Service(BaseModel):
    protocol: Literal["tcp", "udp", "tcp-udp", "sctp"]
    source: Optional[L4ServiceSource] = None
    destination: Optional[L4ServiceDestination] = None


type Protocol = str


type Service = Union[
    L4Service,
    IcmpService,
    ObjectReference,
    Protocol
]
