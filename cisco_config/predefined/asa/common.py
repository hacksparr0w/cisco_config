from typing import Self

from pydantic import BaseModel

from ...deserialize import Next, Record, Replay, ProgressiveDeserializer
from ...token import Eol, Word


__all__ = (
    "Data",
    "Text"
)


class Data(BaseModel):
    content: bytes

    @classmethod
    def deserialize(cls) -> ProgressiveDeserializer[Self]:
        content = b""

        while True:
            token = yield Next()

            if isinstance(token, Word):
                if token.value == "end":
                    return cls(content=content)

                content += bytes.fromhex(token.value)
            elif not isinstance(token, Eol):
                raise ValueError


class Text(BaseModel):
    content: str

    @classmethod
    def deserialize(cls) -> ProgressiveDeserializer[Self]:
        content = ""

        while True:
            index = yield Record()

            try:
                token = yield Next()
            except EOFError:
                token = None

            if isinstance(token, Eol) or token is None:
                if not content:
                    raise ValueError

                yield Replay(index)

                return cls(content=content)
            elif isinstance(token, Word):
                content += token.value
                continue

            raise ValueError
