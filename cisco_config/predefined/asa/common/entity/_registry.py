import warnings

from abc import ABC, abstractmethod

from ._object_group import ObjectGroup


__all__ = (
    "EntityNotFoundError",
    "EntityRegistry",
    "SimpleEntityRegistry"
)


class EntityNotFoundError(Exception):
    pass


class EntityRegistry(ABC):
    @abstractmethod
    def get_object_group(self, name: str) -> ObjectGroup:
        raise NotImplementedError

    @staticmethod
    def warn_unavailable():
        warnings.warn(
            "Entity registry is not available for validation, "
            "command argument binding may not work as expected"
        )


class SimpleEntityRegistry(EntityRegistry):
    def __init__(self, object_groups: list[ObjectGroup]) -> None:
        self._object_groups = {group.name: group for group in object_groups}

    def register_object_group(self, object_group: ObjectGroup) -> None:
        self._object_groups[object_group.name] = object_group

    def get_object_group(self, name: str) -> ObjectGroup:
        try:
            return self._object_groups[name]
        except KeyError as error:
            raise EntityNotFoundError from error

    def delete_object_group(self, name: str) -> ObjectGroup:
        try:
            return self._object_groups.pop(name)
        except KeyError as error:
            raise EntityNotFoundError from error
