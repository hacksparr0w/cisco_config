from typing import Literal

from pydantic import BaseModel, ValidationInfo
from pydantic_core.core_schema import WithInfoValidatorFunction

from ..entity import EntityRegistry, ObjectType


__all__ = (
    "ObjectReference",
    "validate_object_type",
)


class ObjectReference(BaseModel):
    key: Literal["object"] = "object"
    name: str


def validate_object_type(
    type: ObjectType
) -> WithInfoValidatorFunction:
    def validate(
        value: ObjectReference,
        info: ValidationInfo
    ) -> ObjectReference:
        registry = info.context.get("entity_registry") \
            if info.context else None

        if not registry:
            EntityRegistry.warn_unavailable()

            return value

        object = registry.get_object(value.name)

        if object.type != type:
            raise ValueError(
                f"Object group '{value.name}' is not of type '{type}'"
            )

        return value

    return validate
