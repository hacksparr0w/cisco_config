import warnings

from abc import ABC, abstractmethod
from typing import Iterable

from ._object_group import ObjectGroup
from ._object import Object


__all__ = (
    "DuplicateEntityError",
    "EntityNotFoundError",
    "EntityRegistry",
    "SimpleEntityRegistry"
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
    def register_object(self, object: Object) -> None:
        raise NotImplementedError

    @abstractmethod
    def register_object_group(self, object_group: ObjectGroup) -> None:
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

    def register_object(self, object: Object) -> None:
        if object.name in self._objects:
            raise DuplicateEntityError

        self._objects[object.name] = object

    def register_object_group(self, object_group: ObjectGroup) -> None:
        if object_group.name in self._object_groups:
            raise DuplicateEntityError

        self._object_groups[object_group.name] = object_group

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
