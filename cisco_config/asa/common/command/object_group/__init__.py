from typing import TypeAlias, Union

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
