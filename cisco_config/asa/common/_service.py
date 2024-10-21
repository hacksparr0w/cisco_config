from typing import Literal, Optional

from pydantic import BaseModel

from ._base import Key
from ._icmp import IcmpOptions
from ._operator import Operator


__all__ = (
    "IcmpService",
    "L4Service",
    "L4ServiceDestination",
    "L4ServiceSource"
)


class IcmpService(BaseModel):
    type: tuple[Literal["icmp", "icmp6"]]
    options: Optional[IcmpOptions] = None


class L4ServiceSource(BaseModel):
    key: Key["source"]
    value: Operator


class L4ServiceDestination(BaseModel):
    key: Key["destination"]
    value: Operator


class L4Service(BaseModel):
    protocol: Literal["tcp", "udp", "tcp-udp", "sctp"]
    source: Optional[L4ServiceSource] = None
    destination: Optional[L4ServiceDestination] = None
