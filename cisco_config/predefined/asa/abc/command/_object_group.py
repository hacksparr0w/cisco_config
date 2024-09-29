from typing import Literal

from pydantic import BaseModel, ValidationInfo, WithInfoValidatorFunction

from ..entity import EntityRegistry, ObjectGroupType


__all__ = (
    "ObjectGroupReference",
    "validate_object_group_type"
)


class ObjectGroupReference(BaseModel):
    anchor: Literal["object-group"] = "object-group"
    name: str


def validate_object_group_type(
    type: ObjectGroupType
) -> WithInfoValidatorFunction:

    def validate(
        value: ObjectGroupReference,
        info: ValidationInfo
    ) -> ObjectGroupReference:
        registry = info.context.get("entity_registry") \
            if info.context else None

        if not registry:
            EntityRegistry.warn_unavailable()

            return value

        object_group = registry.get_object_group(value.name)

        if object_group.type != type:
            raise ValueError(
                f"Object group '{value.name}' is not of type '{type}'"
            )

        return value

    return validate
