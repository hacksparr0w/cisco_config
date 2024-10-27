from ipaddress import IPv4Address as Ipv4Address

from pydantic import BaseModel


__all__ = (
    "Ipv4Subnet",
)


class Ipv4Subnet(BaseModel):
    address: Ipv4Address
    mask: Ipv4Address
