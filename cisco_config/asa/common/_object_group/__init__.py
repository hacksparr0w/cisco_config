from typing import Union

from . import (
    _model,
    _network,
    _protocol,
    _reference,
    _search,
    _service
)

from ._model import *
from ._network import *
from ._protocol import *
from ._reference import *
from ._search import *
from ._service import *


__all__ = (
    *_model.__all__,
    *_network.__all__,
    *_protocol.__all__,
    *_reference.__all__,
    *_search.__all__,
    *_service.__all__,
    "ObjectGroupCommand"
)


ObjectGroupCommand = Union[
    NetworkObjectGroupCommand,
    ProtocolObjectGroupCommand,
    ServiceObjectGroupCommand
]
