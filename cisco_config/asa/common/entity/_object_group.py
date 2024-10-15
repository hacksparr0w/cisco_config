from enum import StrEnum

from pydantic import BaseModel


__all__ = (
    "ObjectGroup",
    "ObjectGroupType"
)


class ObjectGroupType(StrEnum):
    PROTOCOL = "protocol"
    NETWORK = "network"
    ICMP = "icmp-type"
    SECURITY = "security"
    USER = "user"
    NETWORK_SERVICE = "network-service"
    SERVICE = "service"


class ObjectGroup(BaseModel):
    name: str
    type: ObjectGroupType
