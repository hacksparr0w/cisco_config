from io import StringIO, TextIOBase
from typing import Optional

from .command import Command, deserialize_command
from .deserialization import (
    Context,
    Cut,
    Next,
    ProgressiveDeserializer,
    Record,
    Replay
)

from .stream import ReplayableIterator
from .token import Token, token_reader


__all__ = (
    "load",
    "loads"
)


def _consume(
    deserializer: ProgressiveDeserializer[tuple[Optional[Command], bool]],
    stream: ReplayableIterator[Token]
) -> tuple[Optional[Command], bool]:
    try:
        request = next(deserializer)

        while True:
            if isinstance(request, Cut):
                stream.cut()

                request = deserializer.send(None)
            elif isinstance(request, Next):
                try:
                    token = next(stream)
                except StopIteration:
                    request = deserializer.throw(EOFError)
                else:
                    request = deserializer.send(token)
            elif isinstance(request, Record):
                request = deserializer.send(stream.record())
            elif isinstance(request, Replay):
                index = request.index

                if stream.has_recorded(index):
                    stream.replay(index)

                request = deserializer.send(None)
            else:
                raise TypeError
    except StopIteration as error:
        return error.value


def load(
    hints: tuple[type[Command], ...],
    source: TextIOBase,
    context: Optional[Context] = None
) -> list[Command]:
    reader = token_reader(source)
    stream = ReplayableIterator(reader)
    commands = []

    while True:
        deserializer = deserialize_command(hints, context=context)
        command, eof = _consume(deserializer, stream)

        if command is not None:
            commands.append(command)

        if eof:
            break

    return commands


def loads(
    hints: tuple[type[Command], ...],
    data: str,
    context: Optional[Context] = None
) -> list[Command]:
    return load(hints, StringIO(data), context=context)
