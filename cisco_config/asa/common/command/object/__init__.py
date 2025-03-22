from typing import Union
from typing_extensions import TypeAlias

from . import (
    network,
    service
)


__all__ = (
    "network",
    "service",

    "Object"
)


Object: TypeAlias = Union[
    network.NetworkObject,
    service.ServiceObject
]
