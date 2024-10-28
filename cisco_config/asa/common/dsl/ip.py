from ipaddress import IPv4Address as Ipv4Address

from typing import TypeAlias, Union

from pydantic import BaseModel

from ....command import Key


__all__ = (
    "IpAddressClusterPool",
    "IpAddressFailover",
    "IpAddressStandby"
)


class IpAddressClusterPool(BaseModel):
    key: Key["cluster-pool"]
    name: str


class IpAddressStandby(BaseModel):
    key: Key["standby"]
    address: Ipv4Address


IpAddressFailover: TypeAlias = Union[
    IpAddressClusterPool,
    IpAddressStandby
]
