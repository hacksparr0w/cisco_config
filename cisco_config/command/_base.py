from __future__ import annotations

from typing import Any

from pydantic import BaseModel


__all__ = (
    "Argument",
    "Command"
)


class Argument(BaseModel):
    name: str
    value: Any


class Command(BaseModel):
    name: str
    arguments: list[Argument]
    subcommands: list[Command]
