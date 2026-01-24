from typing import Union
from typing_extensions import TypeAlias

from . import (
    network,
    protocol,
    icmp_type,
    search,
    service
)


__all__ = (
    "network",
    "protocol",
    "icmp_type",
    "search",
    "service",
    "ObjectGroup"
)


ObjectGroup: TypeAlias = Union[
    network.NetworkObjectGroup,
    protocol.ProtocolObjectGroup,
    service.ServiceObjectGroup,
    icmp_type.IcmpObjectGroup
]
