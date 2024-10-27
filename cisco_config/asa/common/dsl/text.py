from typing import Optional, Self

from pydantic import BaseModel

from ....deserialization import (
    Context,
    Next,
    ProgressiveDeserializer,
    Record,
    Replay
)

from ....token import Eol, Word


__all__ = (
    "Text",
)


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
