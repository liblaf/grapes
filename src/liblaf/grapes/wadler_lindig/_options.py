from typing import Any, Unpack, cast

import tlz
import wadler_lindig as wl

from liblaf.grapes._config import config

from ._typing import WadlerLindigOptions
from .custom import chain_custom, pdoc_custom


def make_kwargs(**kwargs: Unpack[WadlerLindigOptions]) -> WadlerLindigOptions:
    kwargs: dict[str, Any] = tlz.merge(config.pretty.get(), kwargs)
    prelude_custom = _PreludeCustom(kwargs)
    kwargs["custom"] = chain_custom(kwargs.get("custom"), prelude_custom)
    return cast("WadlerLindigOptions", kwargs)


class _PreludeCustom:
    kwargs: dict[str, Any]  # keep a reference to use updated kwargs

    def __init__(self, kwargs: dict[str, Any]) -> None:
        self.kwargs = kwargs

    def __call__(self, *args: Any, **kwargs: Any) -> wl.AbstractDoc | None:
        kwargs: dict[str, Any] = {**self.kwargs, **kwargs}
        return pdoc_custom(*args, **kwargs)
