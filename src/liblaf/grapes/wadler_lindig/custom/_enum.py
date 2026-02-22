import enum
from typing import Unpack

import wadler_lindig as wl

from liblaf.grapes.wadler_lindig._typing import WadlerLindigOptions

from ._type import pdoc_type


def pdoc_enum(obj: enum.Enum, **kwargs: Unpack[WadlerLindigOptions]) -> wl.AbstractDoc:
    return pdoc_type(type(obj), dataclass=True, **kwargs) + wl.TextDoc(f".{obj.name}")
