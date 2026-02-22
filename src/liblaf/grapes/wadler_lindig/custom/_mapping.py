from collections.abc import Mapping
from typing import Any, Unpack

import wadler_lindig as wl

from liblaf.grapes.wadler_lindig._typing import WadlerLindigOptions

from ._type import pdoc_type


def pdoc_mapping(
    obj: Mapping[Any, Any], **kwargs: Unpack[WadlerLindigOptions]
) -> wl.AbstractDoc:
    if type(obj) is dict:
        begin: wl.AbstractDoc = wl.TextDoc("{")
    else:
        begin: wl.AbstractDoc = pdoc_type(
            type(obj), dataclass=True, **kwargs
        ) + wl.TextDoc("{")
    return wl.bracketed(
        begin=begin,
        docs=[
            wl.pdoc(key, **kwargs) + wl.TextDoc(": ") + wl.pdoc(value, **kwargs)
            for key, value in obj.items()
        ],
        sep=wl.comma,
        end=wl.TextDoc("}"),
        indent=kwargs.get("indent", 2),
    )
