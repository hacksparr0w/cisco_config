from typing import Literal, Union

from ....command import Command

from ._base import No


__all__ = (
    "ObjectGroupSearchCommand",
)


class ObjectGroupSearchCommand(Command):
    no: No
    key: Literal["object-group-search"] = "object-group-search"
    type: Union[Literal["access-control"], Literal["threshold"]]
