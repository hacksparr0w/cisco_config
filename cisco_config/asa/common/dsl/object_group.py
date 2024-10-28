from pydantic import BaseModel

from ....command import Key


__all__ = (
    "ObjectGroup",
    "NetworkServiceObjectGroup",
    "SecurityObjectGroup",
    "UserObjectGroup"
)


class ObjectGroup(BaseModel):
    key: Key["object-group"]
    name: str


class NetworkServiceObjectGroup(BaseModel):
    key: Key["object-group-network-service"]
    name: str


class SecurityObjectGroup(BaseModel):
    key: Key["object-group-security"]
    name: str


class UserObjectGroup(BaseModel):
    key: Key["object-group-user"]
    name: str
