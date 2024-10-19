from typing import Literal, Optional

from pydantic import BaseModel

from ...command import Command


__all__ = (
    "AutoMacAddressCommand",
    "AutoMacAddressRemoveCommand",
    "MacAddressPrefix"
)


class MacAddressPrefix(BaseModel):
    key: Literal["prefix"]
    prefix: int


class AutoMacAddressCommand(Command):
    key: tuple[Literal["mac-address"], Literal["auto"]] = (
        "mac-address",
        "auto"
    )

    prefix: Optional[MacAddressPrefix] = None


class AutoMacAddressRemoveCommand(Command):
    key: tuple[Literal["no"], Literal["mac-address"], Literal["auto"]] = (
        "no",
        "mac-address",
        "auto"
    )
