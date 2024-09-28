from io import StringIO
from typing import Optional

from .command import Command, deserialize_command
from .deserialization import (
    Cut,
    Next,
    ProgressiveDeserializer,
    Record,
    Replay
)

from .stream import ReplayableIterator
from .token import Token, TokenReader, token_reader


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
                request = deserializer.send(stream.cut())
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


def load(hints: tuple[Command, ...], reader: TokenReader) -> list[Command]:
    result = []
    stream = ReplayableIterator(reader)

    while True:
        command, eof = _consume(deserialize_command(hints), stream)

        if command is not None:
            result.append(command)

        if eof:
            break

    return result


def loads(
    hints: tuple[Command, ...],
    data: str
) -> list[Command]:
    return load(hints, token_reader(StringIO(data)))
