from ipaddress import IPv4Address

from typing import Literal

from pydantic import BaseModel


__all__ = (
    "Host",
)


class Host(BaseModel):
    key: Literal["host"] = "host"
    value: IPv4Address
