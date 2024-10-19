import importlib

from io import TextIOBase
from typing import Generator

from ..command import Command
from ..loading import load as _load

from .common import (
    EntityRegistry,
    SimpleEntityRegistry,
    ObjectCommand,
    ObjectGroupCommand
)


__all__ = (
    "load",
    "Loader"
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


Loader = Generator[Command, None, EntityRegistry]


def load(version: str, source: TextIOBase, strict: bool = False) -> Loader:
    entity_registry = SimpleEntityRegistry()
    context = {"entity_registry": entity_registry}
    hints = _import_hints(version)
    commands = _load(hints, source, strict=strict, context=context)

    for command in commands:
        if isinstance(command, ObjectCommand):
            entity_registry.register_object(command)
        elif isinstance(command, ObjectGroupCommand):
            entity_registry.register_object_group(command)

        yield command

    return entity_registry