from typing_extensions import Self
from typing import Optional

from pydantic import BaseModel

from ....deserialization import Context, Next, ProgressiveDeserializer
from ....token import Eol, Word


__all__ = (
    "Data",
)


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
