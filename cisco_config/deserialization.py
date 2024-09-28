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
    "ProgressiveDeserializer",
    "ProgressiveDeserializerRequest",
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


type ProgressiveDeserializerRequest = Union[Next, Record, Replay]
type ProgressiveDeserializer[T] = Generator[
    ProgressiveDeserializerRequest,
    Any,
    T
]


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
    return int((yield from deserialize_string()))


def deserialize_float() -> ProgressiveDeserializer[float]:
    return float((yield from deserialize_string()))


def deserialize_none() -> ProgressiveDeserializer[None]:
    yield from ()
    return None


def deserialize_union(
    members: tuple[type, ...]
) -> ProgressiveDeserializer[Any]:
    index = yield Record()
    reason = None

    for member in members:
        try:
            return (yield from deserialize(member))
        except (ValueError, EOFError) as error:
            reason = error

            yield Replay(index=index)

    raise ValueError from reason


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
        name: field.annotation for name, field in hint.model_fields.items()
    }

    data = yield from deserialize_object(fields)

    return hint.model_validate(data)


def deserialize(hint: type) -> ProgressiveDeserializer[Any]:
    if get_generic_origin(hint) is Literal:
        return (yield from deserialize_literal(get_generic_args(hint)))
    elif get_generic_origin(hint) is Union:
        return (yield from deserialize_union(get_generic_args(hint)))
    elif issubclass(hint, Deserializable):
        return (yield from hint.deserialize())
    elif issubclass(hint, BaseModel):
        return (yield from deserialize_base_model(hint))
    elif hint is str:
        return (yield from deserialize_string())
    elif hint is int:
        return (yield from deserialize_integer())
    elif hint is float:
        return (yield from deserialize_float())
    elif hint is type(None):
        return (yield from deserialize_none())
    else:
        raise TypeError
