from typing import Union
from typing_extensions import TypeAlias

from . import (
    network,
    protocol,
    search,
    service
)


__all__ = (
    "network",
    "protocol",
    "search",
    "service",
    "ObjectGroup"
)


ObjectGroup: TypeAlias = Union[
    network.NetworkObjectGroup,
    protocol.ProtocolObjectGroup,
    service.ServiceObjectGroup
]
