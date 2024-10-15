from typing import Literal

from ....command import Command


__all__ = (
    "DomainNameCommand",
)


class DomainNameCommand(Command):
    key: Literal["domain-name"] = "domain-name"
    value: str
