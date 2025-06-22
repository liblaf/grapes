import functools
from collections.abc import Callable, Iterable, Sequence
from typing import Any, overload

from liblaf.grapes.logging import depth_tracker

from ._base import BaseTimer, Callback
from ._function import TimedFunction
from ._iterable import TimedIterable
from ._timer import Timer


@functools.singledispatch
@depth_tracker
def _timer_dispatch(_: Any, /, *_args, **_kwargs) -> Any:
    raise TypeError


@_timer_dispatch.register(str)
@depth_tracker
def _(label: str, /, **kwargs) -> Timer:
    return Timer(label=label, **kwargs)


@_timer_dispatch.register(Callable)  # pyright: ignore[reportArgumentType, reportCallIssue]
@depth_tracker
def _(fn: Callable, /, **kwargs) -> TimedFunction:
    return TimedFunction(fn, timing=BaseTimer(**kwargs))


@_timer_dispatch.register(Iterable)
@depth_tracker
def _(iterable: Iterable, /, *, total: int | None = None, **kwargs) -> TimedIterable:
    return TimedIterable(iterable, timing=BaseTimer(**kwargs), total=total)


@overload
def timer[**P, T](
    label: str | None = None,
    *,
    timers: Sequence[str] = ("perf",),
    cb_finish: Callback | None = None,
    cb_start: Callback | None = None,
    cb_stop: Callback | None = None,
) -> Timer: ...
@overload
def timer[**P, T](
    fn: Callable[P, T],
    /,
    *,
    label: str | None = None,
    timers: Sequence[str] = ("perf",),
    cb_finish: Callback | None = None,
    cb_start: Callback | None = None,
    cb_stop: Callback | None = None,
) -> TimedFunction[P, T]: ...
@overload
def timer[**P, T](
    iterable: Iterable[T],
    /,
    *,
    label: str | None = None,
    timers: Sequence[str] = ("perf",),
    total: int | None = None,
    cb_finish: Callback | None = None,
    cb_start: Callback | None = None,
    cb_stop: Callback | None = None,
) -> TimedIterable[T]: ...
@depth_tracker
def timer(*args, **kwargs) -> Any:
    if args:
        return _timer_dispatch(*args, **kwargs)
    return Timer(*args, **kwargs)
