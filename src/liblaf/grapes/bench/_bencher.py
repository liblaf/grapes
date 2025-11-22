import functools
import time
from collections.abc import Callable, Iterable, Mapping, Sequence
from typing import Any, overload

import attrs

from ._results import BenchResults


def _default_setup() -> Iterable[tuple[Sequence, Mapping]]:
    yield (), {}


def _default_size_fn(*_args, **_kwargs) -> int:
    return 1


@attrs.define
class Bencher:
    min_time: float = 0.2
    warmup: int = 2
    _registry: dict[str, Callable] = attrs.field(init=False, factory=dict)
    _setup: Callable[..., Iterable[tuple[Sequence, Mapping]]] = attrs.field(
        default=_default_setup, init=False
    )
    _size_fn: Callable[..., float] = attrs.field(default=_default_size_fn, init=False)

    @overload
    def bench[C: Callable](self, func: C, /, *, label: str | None = None) -> C: ...
    @overload
    def bench[C: Callable](self, *, label: str | None = None) -> Callable[[C], C]: ...
    def bench(
        self, func: Callable | None = None, *, label: str | None = None
    ) -> Callable:
        if func is None:
            return functools.partial(self.bench, label=label)
        if label is None:
            label = func.__name__
        self._registry[label] = func
        return func

    def setup[C: Callable[..., Iterable[tuple[Sequence, Mapping]]]](self, func: C) -> C:
        self._setup = func
        return func

    def size[C: Callable[..., float]](self, func: C) -> C:
        self._size_fn = func
        return func

    def run(self) -> BenchResults:
        inputs: list[tuple[Sequence, Mapping]] = list(self._setup())
        sizes: list[float] = [self._size_fn(*args, **kwargs) for args, kwargs in inputs]
        results: dict[str, Any] = {}
        timings: dict[str, list[float]] = {}
        for name, func in self._registry.items():
            timings_name: list[float] = []
            for args, kwargs in inputs:
                elapsed: float
                results[name], elapsed = self._bench(func, *args, **kwargs)
                timings_name.append(elapsed)
            timings[name] = timings_name
        return BenchResults(results=results, sizes=sizes, timings=timings)

    def _bench[**P, T](
        self, func: Callable[P, T], *args: P.args, **kwargs: P.kwargs
    ) -> tuple[Any, float]:
        for _ in range(self.warmup):
            func(*args, **kwargs)
        count: int = 0
        result: Any = None
        total_time: float = 0.0
        while total_time < self.min_time:
            start: float = time.perf_counter()
            result = func(*args, **kwargs)
            end: float = time.perf_counter()
            count += 1
            total_time += end - start
        return result, total_time / count
