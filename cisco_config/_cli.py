import importlib
import sys

from io import TextIOBase
from typing import Any, Callable, Iterator, List

import click

from pydantic import TypeAdapter

from .command import Command


def _import_loader(format: str) -> Callable[..., Iterator[Command]]:
    name, version = format.split("/")
    module = importlib.import_module(f".{name}", __package__)

    def load(*args, **kwargs):
        return module.load(version[1:], *args, **kwargs)

    return load


@click.group()
def cli() -> None:
    pass


@cli.command()
@click.argument(
    "source",
    metavar="input",
    type=click.File("r", encoding="utf-8"),
    default=sys.stdin
)
@click.option(
    "--format",
    default="asa/v9.20",
    help="Cisco configuration format"
)
@click.option(
    "--strict",
    is_flag=True,
    default=False
)
def load(source: TextIOBase, format: str, strict: bool) -> None:
    """
    Loads a Cisco configuration and prints the parsed commands as JSON
    """

    loader = _import_loader(format)
    commands = list(loader(source, strict=strict))
    data = TypeAdapter(List[Any]).dump_json(commands, indent=2)

    click.echo(data)
