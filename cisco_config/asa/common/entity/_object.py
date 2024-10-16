from enum import StrEnum

from pydantic import BaseModel


class ObjectType(StrEnum):
    NETWORK = "network"
    NETWORK_SERVICE = "network-service"
    SERVICE = "service"


class Object(BaseModel):
    type: ObjectType
    name: str
