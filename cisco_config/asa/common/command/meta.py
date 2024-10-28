from typing import Optional

from ....command import Command, Key


__all__ = (
    "AsaVersion",
)


class AsaVersion(Command):
    key: Key["ASA", "Version"]
    value: str
    environment: Optional[str] = None
