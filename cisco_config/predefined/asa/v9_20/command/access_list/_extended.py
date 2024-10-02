from typing import Literal, Optional

from ....common.command import (
    Line,
    Log,
    Network,
    Port,
    SecurityObjectGroupReference,
    TimeRangeReference,
    User
)

from ......command import Command


__all__ = (
    "PortfulExtendedAccessListCommand",
    "PortlessExtendedAccessListCommand"
)


class PortfulExtendedAccessListCommand(Command):
    key: Literal["access-list"] = "access-list"
    name: str
    line: Optional[Line] = None
    type: Literal["extended"] = "extended"
    action: Literal["deny", "permit"]
    protocol: Literal["TCP", "UDP", "SCTP"]
    user: Optional[User] = None
    source_security_group: Optional[SecurityObjectGroupReference] = None
    source: Network
    source_port: Optional[Port] = None
    destination_security_group: Optional[SecurityObjectGroupReference] = None
    destination: Network
    destination_port: Optional[Port] = None
    log: Optional[Log] = None
    time_range: Optional[TimeRangeReference] = None
    inactive: Optional[Literal["inactive"]] = None


class PortlessExtendedAccessListCommand(Command):
    key: Literal["access-list"] = "access-list"
    name: str
    line: Optional[Line] = None
    type: Literal["extended"] = "extended"
    action: Literal["deny", "permit"]
    protocol: str
    user: Optional[User] = None
    source_security_group: Optional[SecurityObjectGroupReference] = None
    source: Network
    destination_security_group: Optional[SecurityObjectGroupReference] = None
    destination: Network
    log: Optional[Log] = None
    time_range: Optional[TimeRangeReference] = None
    inactive: Optional[Literal["inactive"]] = None
