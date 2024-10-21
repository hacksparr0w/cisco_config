from pydantic import BaseModel

from .._base import Key


__all__ = (
    "NetworkServiceObjectGroupReference",
    "ObjectGroupReference",
    "SecurityObjectGroupReference",
    "UserObjectGroupReference"
)


class ObjectGroupReference(BaseModel):
    key: Key["object-group"]
    name: str


class NetworkServiceObjectGroupReference(BaseModel):
    key: Key["object-group-network-service"]
    name: str


class SecurityObjectGroupReference(BaseModel):
    key: Key["object-group-security"]
    name: str


class UserObjectGroupReference(BaseModel):
    key: Key["object-group-user"]
    name: str
