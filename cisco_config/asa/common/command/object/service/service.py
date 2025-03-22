from typing import Literal, Optional, Tuple, Union
from typing_extensions import TypeAlias

from pydantic import BaseModel

from ......command import Command, Key
from ....dsl.op import Op
from ....dsl.icmp import IcmpOptions


__all__ = (
    "IcmpServiceSpec",
    "L4ServiceSpec",
    "ModifyService",
    "RemoveService",
    "Service",
    "ServiceSpec"
)


class L4ServiceSpec(BaseModel):
    protocol: Union[Literal["tcp"], Literal["udp"], Literal["sctp"]]
    source: Optional[Tuple[Literal["source"], Op]] = None
    destination: Optional[Tuple[Literal["destination"], Op]] = None


class IcmpServiceSpec(BaseModel):
    protocol: Union[Literal["icmp"], Literal["icmp6"]]
    options: IcmpOptions


ServiceSpec: TypeAlias = Union[
    int,
    L4ServiceSpec,
    IcmpServiceSpec
]


class Service(Command):
    key: Key["service"]
    spec: ServiceSpec


class RemoveService(Command):
    key: Key["no", "service"]
    spec: ServiceSpec


ModifyService: TypeAlias = Union[
    Service,
    RemoveService
]
