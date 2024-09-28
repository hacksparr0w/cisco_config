from typing import Literal, Optional, Union

from ._base import (
    Line,
    Log,
    NetworkTarget,
    ObjectGroupSecurityReference,
    Port,
    TimeRangeReference,
    UserTarget
)

from .....command import Command


__all__ = (
    "PortfulExtendedAccessListCommand",
    "PortlessExtendedAccessListCommand"
)


class PortfulExtendedAccessListCommand(Command):
    name: Literal["access-list"] = "access-list"
    id: str
    line: Optional[Line] = None
    type: Literal["extended"] = "extended"
    action: Literal["deny", "permit"]
    protocol: Literal["TCP", "UDP", "SCTP"]
    user: Optional[UserTarget] = None
    source_security_group: Optional[ObjectGroupSecurityReference] = None
    source: NetworkTarget
    source_port: Optional[Port] = None
    destination_security_group: Optional[ObjectGroupSecurityReference] = None
    destination: NetworkTarget
    destination_port: Optional[Port] = None
    log: Optional[Log] = None
    time_range: Optional[TimeRangeReference] = None
    inactive: Optional[Literal["inactive"]] = None


class PortlessExtendedAccessListCommand(Command):
    name: Literal["access-list"] = "access-list"
    id: str
    line: Optional[Line] = None
    type: Literal["extended"] = "extended"
    action: Literal["deny", "permit"]
    protocol: str
    user: Optional[UserTarget] = None
    source_security_group: Optional[ObjectGroupSecurityReference] = None
    source: NetworkTarget
    destination_security_group: Optional[ObjectGroupSecurityReference] = None
    destination: NetworkTarget
    log: Optional[Log] = None
    time_range: Optional[TimeRangeReference] = None
    inactive: Optional[Literal["inactive"]] = None
