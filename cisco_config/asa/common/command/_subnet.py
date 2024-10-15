from ipaddress import IPv4Address

from pydantic import BaseModel


__all__ = (
    "IPv4Subnet",
)


class IPv4Subnet(BaseModel):
    address: IPv4Address
    mask: IPv4Address
