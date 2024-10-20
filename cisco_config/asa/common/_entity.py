import warnings

from abc import ABC, abstractmethod
from typing import Iterable, Optional

from pydantic import ValidationInfo
from pydantic_core.core_schema import WithInfoValidatorFunction

from ._base import Named
from ._object import NetworkObjectCommand, Object, ObjectCommand, ObjectType
from ._object_group import (
    NetworkObjectGroupCommand,
    ObjectGroup,
    ObjectGroupCommand,
    ObjectGroupType,
    ProtocolObjectGroupCommand,
    ServiceObjectGroupCommand
)


__all__ = (
    "DuplicateEntityError",
    "EntityNotFoundError",
    "EntityRegistry",
    "SimpleEntityRegistry",

    "get_entity_registry",
    "validate_object_group_type",
    "validate_object_type"
)


class DuplicateEntityError(Exception):
    pass


class EntityNotFoundError(Exception):
    pass


class EntityRegistry(ABC):
    @abstractmethod
    def delete_object(self, name: str) -> Object:
        raise NotImplementedError

    @abstractmethod
    def delete_object_group(self, name: str) -> ObjectGroup:
        raise NotImplementedError

    @abstractmethod
    def get_object(self, name: str) -> Object:
        raise NotImplementedError

    @abstractmethod
    def get_object_group(self, name: str) -> ObjectGroup:
        raise NotImplementedError

    @abstractmethod
    def register_object(self, command: ObjectCommand) -> Object:
        raise NotImplementedError

    @abstractmethod
    def register_object_group(
        self,
        command: ObjectGroupCommand
    ) -> ObjectGroup:
        raise NotImplementedError

    @staticmethod
    def warn_unavailable() -> None:
        warnings.warn(
            "Entity registry is not available for validation, "
            "command argument binding may not work as expected"
        )


class SimpleEntityRegistry(EntityRegistry):
    def __init__(
        self,
        objects: Iterable[Object] = [],
        object_groups: Iterable[ObjectGroup] = []
    ) -> None:
        self._objects = {object.name: object for object in objects}
        self._object_groups = {group.name: group for group in object_groups}

    @staticmethod
    def create_object(command: ObjectCommand) -> Object:
        match command:
            case NetworkObjectCommand(name=name):
                return Object(type=ObjectType.NETWORK, name=name)
            case _:
                raise TypeError
    
    @staticmethod
    def create_object_group(command: ObjectGroupCommand) -> ObjectGroup:
        match command:
            case NetworkObjectGroupCommand(name=name):
                return ObjectGroup(type=ObjectGroupType.NETWORK, name=name)
            case ProtocolObjectGroupCommand(name=name):
                return ObjectGroup(type=ObjectGroupType.PROTOCOL, name=name)
            case ServiceObjectGroupCommand(name=name):
                return ObjectGroup(type=ObjectGroupType.SERVICE, name=name)
            case _:
                raise TypeError

    def get_object(self, name: str) -> Object:
        try:
            return self._objects[name]
        except KeyError as error:
            raise EntityNotFoundError from error

    def get_object_group(self, name: str) -> ObjectGroup:
        try:
            return self._object_groups[name]
        except KeyError as error:
            raise EntityNotFoundError from error

    def register_object(self, command: ObjectCommand) -> Object:
        object = self.create_object(command)

        if object.name in self._objects:
            raise DuplicateEntityError

        self._objects[object.name] = object

        return object

    def register_object_group(
        self,
        command: ObjectGroupCommand
    ) -> ObjectGroup:
        object_group = self.create_object_group(command)

        if object_group.name in self._object_groups:
            raise DuplicateEntityError

        self._object_groups[object_group.name] = object_group

        return object_group

    def delete_object(self, name: str) -> Object:
        try:
            return self._objects.pop(name)
        except KeyError as error:
            raise EntityNotFoundError from error

    def delete_object_group(self, name: str) -> ObjectGroup:
        try:
            return self._object_groups.pop(name)
        except KeyError as error:
            raise EntityNotFoundError from error


def get_entity_registry(info: ValidationInfo) -> Optional[EntityRegistry]:
    registry = info.context.get("entity_registry") if info.context else None

    if not registry:
        EntityRegistry.warn_unavailable()

    return registry


def validate_object_type(type: ObjectType) -> WithInfoValidatorFunction:
    def validate[T: Named](value: T, info: ValidationInfo) -> T:
        registry = get_entity_registry(info)

        if not registry:
            return value

        object = registry.get_object(value.name)

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
        registry = get_entity_registry(info)

        if not registry:
            return value

        object_group = registry.get_object_group(value.name)

        if object_group.type != type:
            raise ValueError(
                f"Object group '{value.name}' is not of type '{type}'"
            )

        return value

    return validate
