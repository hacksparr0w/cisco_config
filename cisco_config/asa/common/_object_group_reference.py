from typing import Literal

from pydantic import BaseModel


__all__ = (
    "ObjectGroupReference",
    "SecurityObjectGroupReference",
    "UserObjectGroupReference",
    "NetworkServiceObjectGroupReference",
)


class ObjectGroupReference(BaseModel):
    key: Literal["object-group"] = "object-group"
    name: str


class NetworkServiceObjectGroupReference(BaseModel):
    key: Literal["object-group-network-service"] = \
        "object-group-network-service"

    name: str


class SecurityObjectGroupReference(BaseModel):
    key: Literal["object-group-security"] = "object-group-security"
    name: str


class UserObjectGroupReference(BaseModel):
    key: Literal["object-group-user"] = "object-group-user"
    name: str
