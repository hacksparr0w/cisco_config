from typing import Literal

from ...command import Command
from ._domain_name import DomainNameCommand


__all__ = (
    "DnsServerGroupCommand",
    "DnsServerGroupDomainNameCommand"
)


class DnsServerGroupDomainNameCommand(DomainNameCommand):
    pass


class DnsServerGroupCommand(Command):
    key: tuple[Literal["dns"], Literal["server-group"]] = (
        "dns",
        "server-group"
    )

    name: str
    domain: list[DnsServerGroupDomainNameCommand] = []
