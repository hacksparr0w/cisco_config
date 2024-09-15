from typing import Literal, Optional

from pydantic import BaseModel

from ....command import Parameter, Specification
from ..base import Text


class Line(BaseModel):
    name: Literal["line"]
    number: int


class Remark(BaseModel):
    name: Literal["remark"]
    text: Text


commands = (
    Specification(
        name="access-list",
        parameters=[
            Parameter(name="id", type=str),
            Parameter(name="line", type=Optional[Line]),
            Parameter(name="remark", type=Remark)
        ]
    ),
)
