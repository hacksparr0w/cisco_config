from typing import (
    Any,
    Generator,
    Literal,
    Protocol,
    Self,
    Union,
    get_args as get_generic_args,
    get_origin as get_generic_origin,
    runtime_checkable
)

from pydantic import BaseModel

from .token import Word


__all__ = (
    "Cut",
    "Deserializable",
    "Next",
    "ProgressiveDeserializerMessage",
    "ProgressiveDeserializer",
    "Record",
    "Replay",

    "deserialize",
    "deserialize_base_model",
    "deserialize_float",
    "deserialize_integer",
    "deserialize_literal",
    "deserialize_none",
    "deserialize_object",
    "deserialize_string",
    "deserialize_union"
)


class Cut(BaseModel):
    pass


class Next(BaseModel):
    pass


class Record(BaseModel):
    pass


class Replay(BaseModel):
    index: int


type ProgressiveDeserializerMessage = Union[Next, Record, Replay]
type ProgressiveDeserializer[T] = Generator[None, Any, T]


@runtime_checkable
class Deserializable(Protocol):
    @classmethod
    def deserialize(cls) -> ProgressiveDeserializer[Self]:
        ...


def deserialize_string() -> ProgressiveDeserializer[str]:
    token = yield Next()

    if not isinstance(token, Word):
        raise ValueError

    return token.value


def deserialize_literal(
    members: tuple[str, ...]
) -> ProgressiveDeserializer[str]:
    result = yield from deserialize_string()

    if result not in members:
        raise ValueError

    return result


def deserialize_integer() -> ProgressiveDeserializer[int]:
    result = yield from deserialize_string()

    return int(result)


def deserialize_float() -> ProgressiveDeserializer[float]:
    result = yield from deserialize_string()

    return float(result)


def deserialize_none() -> ProgressiveDeserializer[None]:
    yield from ()
    return None


def deserialize_union(
    members: tuple[type, ...]
) -> ProgressiveDeserializer[Any]:
    index = yield Record()
    error = None

    for member in members:
        try:
            yield from deserialize(member)
        except ValueError as error:
            yield Replay(index=index)

    raise ValueError from error


def deserialize_object(
    fields: dict[str, type]
) -> ProgressiveDeserializer[dict]:
    result = {}

    for name, hint in fields.items():
        result[name] = yield from deserialize(hint)

    return result


def deserialize_base_model(
    hint: type[BaseModel]
) -> ProgressiveDeserializer[BaseModel]:
    fields = {
        name: field.annotation for name, field in hint.__fields__.items()
    }

    data = yield from deserialize_object(fields)

    return hint(**data)


def deserialize(hint: type) -> ProgressiveDeserializer[Any]:
    if issubclass(hint, Deserializable):
        yield from hint.deserialize()
    elif issubclass(hint, BaseModel):
        yield from deserialize_base_model(hint)
    elif hint is str:
        yield from deserialize_string()
    elif hint is int:
        yield from deserialize_integer()
    elif hint is float:
        yield from deserialize_float()
    elif hint is type(None):
        yield from deserialize_none()
    elif get_generic_origin(hint) is Literal:
        yield from deserialize_literal(get_generic_args(hint))
    elif get_generic_origin(hint) is Union:
        yield from deserialize_union(get_generic_args(hint))
    else:
        raise TypeError
