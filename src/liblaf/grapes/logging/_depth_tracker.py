import contextlib
import contextvars
import functools
import types
from collections.abc import Callable
from typing import Self, overload

import attrs

from liblaf.grapes import itertools as _it

_depth: contextvars.ContextVar[int] = contextvars.ContextVar("depth", default=0)


@attrs.define
class DepthTracker(contextlib.AbstractContextManager):
    _depth_inc: int | None = attrs.field(default=None)
    _token: contextvars.Token[int] = attrs.field(default=None)

    def __enter__(self) -> Self:
        self._token = _depth.set(_depth.get() + _it.first_not_none(self._depth_inc, 1))
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: types.TracebackType | None,
        /,
    ) -> None:
        _depth.reset(self._token)
        del self._token

    @overload
    def __call__(self, /, *, depth: int) -> Self: ...
    @overload
    def __call__[**P, T](
        self, func: Callable[P, T], /, *, depth: int | None = None
    ) -> Callable[P, T]: ...
    def __call__[**P, T](
        self, func: Callable[P, T] | None = None, /, *, depth: int | None = None
    ) -> Callable:
        if func is None:
            if depth is None:
                return self
            return attrs.evolve(self, depth_inc=depth)

        @functools.wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            token: contextvars.Token[int] = _depth.set(
                _depth.get() + _it.first_not_none(depth, self._depth_inc, 2)
            )
            try:
                return func(*args, **kwargs)
            finally:
                _depth.reset(token)

        return wrapper

    @property
    def depth(self) -> int:
        return _depth.get()


depth_tracker: DepthTracker = DepthTracker()
