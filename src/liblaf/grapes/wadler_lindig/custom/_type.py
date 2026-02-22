from typing import Unpack

import wadler_lindig as wl
from wadler_lindig._definitions import _pformat_type

from liblaf.grapes.wadler_lindig._typing import WadlerLindigOptions


def pdoc_type(
    obj: type, *, dataclass: bool = False, **kwargs: Unpack[WadlerLindigOptions]
) -> wl.AbstractDoc:
    if dataclass:
        kwargs["show_type_module"] = kwargs.get("show_dataclass_module", False)
    return _pformat_type(obj, **kwargs)
