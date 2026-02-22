from typing import Unpack

import pydantic
import wadler_lindig as wl

from liblaf.grapes.wadler_lindig._typing import WadlerLindigOptions

from ._type import pdoc_type


def pdoc_pydantic_root_model(
    obj: pydantic.RootModel, **kwargs: Unpack[WadlerLindigOptions]
) -> wl.AbstractDoc:
    return pdoc_type(type(obj), dataclass=True, **kwargs) + wl.pdoc(obj.root, **kwargs)
