from typing_extensions import TypeAlias

from . import network


__all__ = (
    "network",

    "Object"
)


Object: TypeAlias = network.NetworkObject
