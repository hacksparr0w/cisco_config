from typing import Literal

from pydantic import BaseModel, ValidationInfo
from pydantic_core.core_schema import WithInfoValidatorFunction

from ..entity import EntityRegistry, ObjectGroupType


__all__ = (
    "ObjectGroupReference",
    "SecurityObjectGroupReference",
    "UserObjectGroupReference",
    "NetworkServiceObjectGroupReference",

    "validate_object_group_type"
)


class ObjectGroupReference(BaseModel):
    key: Literal["object-group"] = "object-group"
    name: str


class NetworkServiceObjectGroupReference(BaseModel):
    key: Literal["object-group-network-service"] = \
        "object-group-network-service"

    name: str


class SecurityObjectGroupReference(BaseModel):
    key: Literal["object-group-security"] = "object-group-security"
    name: str


class UserObjectGroupReference(BaseModel):
    key: Literal["object-group-user"] = "object-group-user"
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
