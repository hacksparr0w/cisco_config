import warnings

from abc import ABC, abstractmethod

from ._object_group import ObjectGroup


__all__ = (
    "EntityNotFoundError",
    "EntityRegistry"
)


class EntityNotFoundError(Exception):
    pass


class EntityRegistry(ABC):
    @abstractmethod
    def get_object_group(name: str) -> ObjectGroup:
        raise NotImplementedError

    @staticmethod
    def warn_unavailable():
        warnings.warn(
            "Entity registry is not available for validation, "
            "command argument binding may not work as expected"
        )
