from abc import ABC, abstractmethod
from typing import Iterable

from .command.object import Object as ObjectCommand
from .command.object.network import NetworkObject as NetworkObjectCommand
from .command.object_group import ObjectGroup as ObjectGroupCommand
from .command.object_group.network import \
    NetworkObjectGroup as NetworkObjectGroupCommand

from .command.object_group.protocol import \
    ProtocolObjectGroup as ProtocolObjectGroupCommand

from .command.object_group.service import \
    ServiceObjectGroup as ServiceObjectGroupCommand

from .entity import (
    Object,
    ObjectGroup,
    ObjectGroupType,
    ObjectType
)


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
    def register_object(self, command: ObjectCommand) -> Object:
        raise NotImplementedError

    @abstractmethod
    def register_object_group(
        self,
        command: ObjectGroupCommand
    ) -> ObjectGroup:
        raise NotImplementedError


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
        if isinstance(command, NetworkObjectCommand):
            return Object(type=ObjectType.NETWORK, name=command.name)
        else:
            raise TypeError
    
    @staticmethod
    def create_object_group(command: ObjectGroupCommand) -> ObjectGroup:
        if isinstance(command, NetworkObjectGroupCommand):
            return ObjectGroup(
                type=ObjectGroupType.NETWORK,
                name=command.name
            )

        elif isinstance(command, ProtocolObjectGroupCommand):
            return ObjectGroup(
                type=ObjectGroupType.PROTOCOL,
                name=command.name
            )

        elif isinstance(command, ServiceObjectGroupCommand):
            return ObjectGroup(
                type=ObjectGroupType.SERVICE,
                name=command.name
            )

        else:
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

        self._objects[object.name] = object

        return object

    def register_object_group(
        self,
        command: ObjectGroupCommand
    ) -> ObjectGroup:
        object_group = self.create_object_group(command)

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
