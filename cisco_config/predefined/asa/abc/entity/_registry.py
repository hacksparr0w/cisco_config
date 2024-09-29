import warnings

from ._object_group import ObjectGroup


class EntityNotFoundError(Exception):
    pass


class EntityRegistry:
    def get_object_group(name: str) -> ObjectGroup:
        raise NotImplementedError

    @staticmethod
    def warn_unavailable():
        warnings.warn(
            "Entity registry is not available for validation, "
            "command argument binding may not work as expected"
        )
