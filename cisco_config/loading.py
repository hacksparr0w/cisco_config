from io import TextIOBase
from typing import Optional, Iterator

from .command import Command, deserialize_command
from .deserialization import (
    Context,
    Next,
    ProgressiveDeserializer,
    Record,
    Replay
)

from .stream import ReplayableIterator
from .token import Token, token_reader


__all__ = (
    "load",
)


def _consume(
    deserializer: ProgressiveDeserializer[tuple[Optional[Command], bool]],
    stream: ReplayableIterator[Token]
) -> tuple[Optional[Command], bool]:
    try:
        request = next(deserializer)

        while True:
            if isinstance(request, Next):
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
    strict: bool = True,
    context: Optional[Context] = None
) -> Iterator[Command]:
    reader = token_reader(source)
    stream = ReplayableIterator(reader)

    while True:
        deserializer = deserialize_command(
            hints,
            strict=strict,
            context=context
        )

        command, eof = _consume(deserializer, stream)

        stream.cut()

        if command is not None:
            yield command

        if eof:
            return
