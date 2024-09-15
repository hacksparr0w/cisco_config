from typing import Any

from __future__ import annotations

from pydantic import BaseModel


__all__ = (
    "Parameter",
    "Specification",
    "Text"
)


class Text(BaseModel):
    content: str


class Parameter(BaseModel):
    name: str
    type: type[Any]


class Specification(BaseModel):
    name: str
    parameters: list[Parameter]
    subcommands: list[Specification]
