import functools
from typing import Unpack

import toolz

from liblaf.grapes._config import config

from ._typing import CustomCallable, WadlerLindigOptions
from .custom import chain_custom, pdoc_custom


def make_kwargs(**kwargs: Unpack[WadlerLindigOptions]) -> WadlerLindigOptions:
    kwargs = toolz.merge(config.pretty.get(), kwargs)
    pdoc_custom_partial: CustomCallable = functools.partial(pdoc_custom, **kwargs)
    kwargs["custom"] = (
        chain_custom(kwargs["custom"], pdoc_custom_partial)
        if "custom" in kwargs
        else pdoc_custom_partial
    )
    return kwargs  # pyright: ignore[reportReturnType]
