from io import StringIO
from typing import Optional

from .command import Command, deserialize_command
from .deserialize import Cut, Next, ProgressiveDeserializer, Record, Replay
from .stream import ReplayableIterator
from .token import Token, TokenReader, token_reader


def _consume(
    deserializer: ProgressiveDeserializer[tuple[Optional[Command], bool]],
    stream: ReplayableIterator[Token]
) -> tuple[Optional[Command], bool]:
    try:
        while True:
            message = next(deserializer)

            if isinstance(message, Cut):
                deserializer.send(stream.cut())
            elif isinstance(message, Next):
                try:
                    deserializer.send(next(stream))
                except StopIteration:
                    deserializer.throw(EOFError)
            elif isinstance(message, Record):
                deserializer.send(stream.record())
            elif isinstance(message, Replay):
                deserializer.send(stream.replay(message.index))
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
