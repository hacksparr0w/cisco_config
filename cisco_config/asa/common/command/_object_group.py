from typing import Literal, Optional, Union

from ....command import Command

from ._base import No
from ._service import Service


__all__ = (
    "ObjectGroupSearchCommand",
    "ServiceObjectGroupCommand",
    "ServiceObjectGroupServiceObjectCommand"
)


class ObjectGroupSearchCommand(Command):
    no: No
    key: Literal["object-group-search"] = "object-group-search"
    type: Union[Literal["access-control"], Literal["threshold"]]


class ServiceObjectGroupServiceObjectCommand(Command):
    key: Literal["service-object"] = "service-object"
    service: Service


class ServiceObjectGroupCommand(Command):
    key: tuple[Literal["object-group"], Literal["service"]] = (
        "object-group",
        "service"
    )

    name: str
    protocol: Optional[Literal["tcp", "udp", "tcp-udp"]] = None
    objects: list[ServiceObjectGroupServiceObjectCommand]
