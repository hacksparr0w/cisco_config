import typing

from pydantic import BaseModel


class Positional(BaseModel):
    name: str


class Literal(BaseModel):
    value: str


class Union(BaseModel):
    members: list[CommandParameter]


type CommandParameter = Union[]
