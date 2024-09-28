from typing import Optional, Self, Union

from pydantic import BaseModel

from .deserialize import (
    Cut,
    Next,
    ProgressiveDeserializer,
    Record,
    Replay,

    deserialize,
    deserialize_base_model
)

from .token import Eol, Word


class Command(BaseModel):
    @staticmethod
    def deserialize(cls) -> ProgressiveDeserializer[Self]:
        return deserialize_base_model(cls)


def _seek() -> ProgressiveDeserializer[None]:
    index = yield Record()

    while True:
        token = yield Next()

        if not isinstance(token, Word):
            yield Cut()
            index = yield Record()
            continue

        break

    yield Cut()
    yield Replay(index)


def deserialize_command(
    hints: tuple[type[Command], ...],
    parent: Optional[Command] = None
) -> ProgressiveDeserializer[tuple[Optional[Command], bool]]:
    try:
        yield from _seek()
    except EOFError:
        return None, True

    try:
        result = yield from deserialize(Union[hints])
    except (ValueError, EOFError):
        if not parent:
            raise

        raise NotImplementedError

    try:
        token = yield Next()

        if not isinstance(token, Eol):
            raise RuntimeError
    except EOFError:
        return result, True

    return result, False
