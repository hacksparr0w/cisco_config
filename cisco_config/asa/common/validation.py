import warnings

from typing import Any, Iterable, Optional, TypeVar

from pydantic import ValidationInfo
from pydantic_core.core_schema import WithInfoValidatorFunction

from .entity import Object, ObjectGroup, ObjectGroupType, ObjectType


__all__ = (
    "Named",

    "validate_object_group_types",
    "validate_object_types"
)


class Named:
    name: str


T = TypeVar("T", bound=Named)


def _get_entity_registry(info: ValidationInfo) -> Optional[Any]:
    registry = info.context.get("entity_registry") if info.context else None

    if not registry:
        warnings.warn(
            "Entity registry is not available for validation, "
            "command argument binding may not work as expected"
        )

    return registry


def validate_object_types(
    *types: Iterable[ObjectType]
) -> WithInfoValidatorFunction:
    def validate(value: T, info: ValidationInfo) -> T:
        registry = _get_entity_registry(info)

        if not registry:
            return value

        object: Object = registry.get_object(value.name)

        if object.type not in types:
            raise ValueError(
                f"Object '{value.name}' is not any of {types}"
            )

        return value

    return validate


def validate_object_group_types(
    *types: Iterable[ObjectGroupType]
) -> WithInfoValidatorFunction:
    def validate(value: T, info: ValidationInfo) -> T:
        registry = _get_entity_registry(info)

        if not registry:
            return value

        object_group: ObjectGroup = registry.get_object_group(value.name)

        if object_group.type not in types:
            raise ValueError(
                f"Object group '{value.name}' is not any of {types}"
            )

        return value

    return validate
