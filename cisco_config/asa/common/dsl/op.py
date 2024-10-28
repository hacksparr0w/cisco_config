from typing import TypeAlias, Union

from pydantic import BaseModel

from ....command import Key


__all__ = (
    "Eq",
    "Gt",
    "Lt",
    "Neq",
    "Op",
    "Range"
)


class Eq(BaseModel):
    key: Key["eq"]
    value: str


class Gt(BaseModel):
    key: Key["gt"]
    value: str


class Lt(BaseModel):
    key: Key["lt"]
    value: str


class Neq(BaseModel):
    key: Key["neq"]
    value: str


class Range(BaseModel):
    key: Key["range"]
    start: int
    stop: int


Op: TypeAlias = Union[Eq, Gt, Lt, Neq, Range]
