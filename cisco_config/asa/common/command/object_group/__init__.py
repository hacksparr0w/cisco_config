from typing import Union

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


ObjectGroup = Union[
    network.NetworkObjectGroup,
    protocol.ProtocolObjectGroup,
    service.ServiceObjectGroup
]
