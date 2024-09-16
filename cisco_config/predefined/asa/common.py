from __future__ import annotations

from pydantic import BaseModel

from ...deserialize import DeserializationError
from ...stream import ReplayableIterator
from ...token import Eol, Token, Word


__all__ = (
    "Data",
    "Text"
)


class Data(BaseModel):
    content: bytes

    @classmethod
    def __deserialize__(cls: Data, stream: ReplayableIterator[Token]) -> Data:
        content = b""

        while True:
            try:
                token = next(stream)
            except StopIteration:
                raise DeserializationError

            if isinstance(token, Word):
                if token.value == "end":
                    return cls(content=content)

                content += bytes.fromhex(token.value)
            elif not isinstance(token, Eol):
                raise DeserializationError


class Text(BaseModel):
    content: str

    @classmethod
    def __deserialize__(cls: Text, stream: ReplayableIterator[Token]) -> Text:
        content = ""

        while True:
            record = stream.start_recording()

            try:
                token = next(stream)
            except StopIteration:
                token = None

            if not isinstance(token, Word):
                if not content:
                    raise DeserializationError

                if stream.has_recorded(record):
                    stream.replay(record)

                return cls(content=content)

            content += token.value
