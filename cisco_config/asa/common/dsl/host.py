from ipaddress import IPv4Address

from pydantic import BaseModel

from ....command import Key


__all__ = (
    "Host",
)


class Host(BaseModel):
    key: Key["host"]
    value: IPv4Address
