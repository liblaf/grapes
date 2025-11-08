import functools
from typing import Any

import attrs

from liblaf.grapes.ext import wadler_lindig as wl
from liblaf.grapes.functools import wraps


@wraps(attrs.define)
def define(maybe_cls: type | None = None, **kwargs) -> Any:
    if maybe_cls is None:
        return functools.partial(define, **kwargs)
    auto_detect: bool = kwargs.get("auto_detect", True)
    repr_: bool | None = kwargs.get("repr")
    if auto_detect and repr_ is None and "__repr__" not in maybe_cls.__dict__:
        repr_ = True
    if repr_:
        maybe_cls.__repr__ = _attrs_repr  # pyright: ignore[reportAttributeAccessIssue]
    return attrs.define(maybe_cls, **kwargs)


def _attrs_repr(self: object) -> str:
    return wl.pformat(self)
