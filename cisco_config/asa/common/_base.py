from typing import Optional, Self

from pydantic import BaseModel

from ...deserialization import (
    Context,
    Next,
    Record,
    Replay,
    ProgressiveDeserializer
)

from ...token import Eol, Word


__all__ = (
    "Data",
    "Named",
    "Text"
)


class Named:
    name: str


class Data(BaseModel):
    content: bytes

    @classmethod
    def deserialize(
        cls,
        context: Optional[Context] = None
    ) -> ProgressiveDeserializer[Self]:
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
    def deserialize(
        cls,
        context: Optional[Context] = None
    ) -> ProgressiveDeserializer[Self]:
        content = ""

        while True:
            index = yield Record()

            try:
                token = yield Next()
            except EOFError:
                token = None

            if isinstance(token, Eol) or token is None:
                yield Replay(index=index)

                return cls(content=content)
            elif isinstance(token, Word):
                if content:
                    content += " "

                content += token.value

                continue

            raise ValueError
