from typing import Literal, Union

from pydantic import BaseModel


__all__ = (
    "Eq",
    "Gt",
    "Lt",
    "Neq",
    "Op",
    "Range"
)


class Eq(BaseModel):
    key: Literal["eq"] = "eq"
    value: str


class Gt(BaseModel):
    key: Literal["gt"] = "gt"
    value: str


class Lt(BaseModel):
    key: Literal["lt"] = "lt"
    value: str


class Neq(BaseModel):
    key: Literal["neq"] = "neq"
    value: str


class Range(BaseModel):
    key: Literal["range"] = "range"
    start: int
    stop: int


Op = Union[Eq, Gt, Lt, Neq, Range]
