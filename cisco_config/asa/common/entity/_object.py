from enum import StrEnum

from pydantic import BaseModel


__all__ = (
    "Object",
    "ObjectType"
)


class ObjectType(StrEnum):
    NETWORK = "network"
    NETWORK_SERVICE = "network-service"
    SERVICE = "service"


class Object(BaseModel):
    type: ObjectType
    name: str
