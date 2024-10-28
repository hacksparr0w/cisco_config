from typing import Literal, Optional

from pydantic import BaseModel

from ....command import Key
from . import icmp, op


__all__ = (
    "IcmpService",
    "L4Service",
    "L4ServiceDestination",
    "L4ServiceSource"
)


class IcmpService(BaseModel):
    type: Literal["icmp", "icmp6"]
    options: Optional[icmp.IcmpOptions] = None


class L4ServiceSource(BaseModel):
    key: Key["source"]
    value: op.Op


class L4ServiceDestination(BaseModel):
    key: Key["destination"]
    value: op.Op


class L4Service(BaseModel):
    protocol: Literal["tcp", "udp", "tcp-udp", "sctp"]
    source: Optional[L4ServiceSource] = None
    destination: Optional[L4ServiceDestination] = None
