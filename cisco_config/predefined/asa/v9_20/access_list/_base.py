from typing import Literal, Optional, Union

from pydantic import BaseModel


__all__ = (
    "Eq",
    "Gt",
    "Host",
    "Line",
    "Log",
    "Lt",
    "LogSpecification",
    "LogSpecificationInterval",
    "Neq",
    "NetworkInterfaceReference",
    "NetworkRange",
    "NetworkTarget",
    "ObjectGroupNetworkServiceReference",
    "ObjectGroupReference",
    "ObjectGroupSecurityReference",
    "ObjectGroupUserReference",
    "ObjectReference",
    "Port",
    "Range",
    "TimeRangeReference",
    "UserGroupReference",
    "UserReference",
    "UserTarget"
)


class Eq(BaseModel):
    name: Literal["eq"] = "eq"
    value: int


class Gt(BaseModel):
    name: Literal["gt"] = "gt"
    value: int


class Lt(BaseModel):
    name: Literal["lt"] = "lt"
    value: int


class Neq(BaseModel):
    name: Literal["neq"] = "neq"
    value: int


class Range(BaseModel):
    name: Literal["range"] = "range"
    start: int
    stop: int


class Host(BaseModel):
    name: Literal["host"] = "host"
    value: str


class Line(BaseModel):
    name: Literal["line"] = "line"
    number: int


class LogSpecificationInterval(BaseModel):
    name: Literal["interval"] = "interval"
    seconds: int


class LogSpecification(BaseModel):
    level: Optional[int] = None
    interval: Optional[LogSpecificationInterval] = None


class Log(BaseModel):
    name: Literal["log"] = "log"
    specification: Union[Literal["disable", "default"], LogSpecification] = \
        LogSpecification()


class NetworkRange(BaseModel):
    ip: str
    mask: str


class NetworkInterfaceReference(BaseModel):
    name: Literal["interface"] = "interface"
    id: str


class ObjectGroupNetworkServiceReference(BaseModel):
    name: Literal["object-group-network-service"] = \
        "object-group-network-service"

    id: str


class ObjectGroupReference(BaseModel):
    name: Literal["object-group"] = "object-group"
    id: str


class ObjectGroupSecurityReference(BaseModel):
    name: Literal["object-group-security"] = "object-group-security"
    id: str


class ObjectGroupUserReference(BaseModel):
    name: Literal["object-group-user"] = "object-group-user"
    id: str


class ObjectReference(BaseModel):
    name: Literal["object"] = "object"
    id: str


class TimeRangeReference(BaseModel):
    name: Literal["time-range"] = "time-range"
    id: str


class UserGroupReference(BaseModel):
    name: Literal["user-group"] = "user-group"
    id: str


class UserReference(BaseModel):
    name: Literal["user"] = "user"
    id: str


NetworkTarget = Union[
    Literal["any", "any4", "any6"],
    Host,
    NetworkInterfaceReference,
    ObjectReference,
    ObjectGroupReference,
    ObjectGroupNetworkServiceReference,
    NetworkRange
]


UserTarget = Union[
    ObjectGroupUserReference,
    UserGroupReference,
    UserReference
]


Port = Union[
    Eq,
    Gt,
    Lt,
    Neq,
    Range,
    ObjectGroupReference
]
