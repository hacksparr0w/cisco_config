import warnings

from typing import Any, Optional

from pydantic import ValidationInfo
from pydantic_core.core_schema import WithInfoValidatorFunction   

from .entity import Object, ObjectGroup, ObjectGroupType, ObjectType


__all__ = (
    "Named",
    "validate_object_group_type",
    "validate_object_type"
)


class Named:
    name: str


def _get_entity_registry(info: ValidationInfo) -> Optional[Any]:
    registry = info.context.get("entity_registry") if info.context else None

    if not registry:
        warnings.warn(
            "Entity registry is not available for validation, "
            "command argument binding may not work as expected"
        )

    return registry


def validate_object_type(type: ObjectType) -> WithInfoValidatorFunction:
    def validate[T: Named](value: T, info: ValidationInfo) -> T:
        registry = _get_entity_registry(info)

        if not registry:
            return value

        object: Object = registry.get_object(value.name)

        if object.type != type:
            raise ValueError(
                f"Object '{value.name}' is not of type '{type}'"
            )

        return value

    return validate


def validate_object_group_type(
    type: ObjectGroupType
) -> WithInfoValidatorFunction:
    def validate[T: Named](value: T, info: ValidationInfo) -> T:
        registry = _get_entity_registry(info)

        if not registry:
            return value

        object_group: ObjectGroup = registry.get_object_group(value.name)

        if object_group.type != type:
            raise ValueError(
                f"Object group '{value.name}' is not of type '{type}'"
            )

        return value

    return validate
