from typing import Literal, Optional

from pydantic import BaseModel

from ...command import Command


__all__ = (
    "MacAddressAutoCommand",
    "MacAddressAutoRemoveCommand",
    "MacAddressPrefix"
)


class MacAddressPrefix(BaseModel):
    key: Literal["prefix"]
    prefix: int


class MacAddressAutoCommand(Command):
    key: tuple[Literal["mac-address"], Literal["auto"]] = (
        "mac-address",
        "auto"
    )

    prefix: Optional[MacAddressPrefix] = None


class MacAddressAutoRemoveCommand(Command):
    key: tuple[Literal["no"], Literal["mac-address"], Literal["auto"]] = (
        "no",
        "mac-address",
        "auto"
    )
