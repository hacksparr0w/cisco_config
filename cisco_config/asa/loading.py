import importlib

from io import TextIOBase
from typing import Iterator

from ..command import Command
from ..loading import load as _load

from .common.command.object import Object as ObjectCommand
from .common.command.object_group import ObjectGroup as ObjectGroupCommand
from .common.entity_registry import SimpleEntityRegistry


__all__ = (
    "load",
)


_HINT_MODULES = {
    "9.20": "v9_20"
}


def _import_hints(version: str) -> tuple[type[Command], ...]:
    name = _HINT_MODULES.get(version)

    if not name:
        raise ValueError(f"Unsupported version 'v{version}'")

    module = importlib.import_module(f".{name}", __package__)
    hints = getattr(module, "hints")

    return hints


def load(
    version: str,
    source: TextIOBase,
    strict: bool = False
) -> Iterator[Command]:
    registry = SimpleEntityRegistry()
    context = {"entity_registry": registry}
    hints = _import_hints(version)
    commands = _load(hints, source, strict=strict, context=context)

    for command in commands:
        if isinstance(command, ObjectCommand):
            registry.register_object(command)
        elif isinstance(command, ObjectGroupCommand):
            registry.register_object_group(command)

        yield command
