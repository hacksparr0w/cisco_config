from typing import Literal, Optional

from pydantic import BaseModel

from ...command import Command


__all__ = (
    "EnablePasswordCommand",
    "PrivilegeLevel"
)


class PrivilegeLevel(BaseModel):
    key: Literal["level"] = "level"
    value: int


class EnablePasswordCommand(Command):
    key: tuple[Literal["enable"], Literal["password"]] = (
        "enable",
        "password"
    )

    value: str
    level: Optional[PrivilegeLevel] = None
    encryption: Optional[Literal["pbkdf2", "encrypted"]] = None
