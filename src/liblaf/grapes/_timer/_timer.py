import atexit
import contextlib
import functools
from collections.abc import Callable, Iterable, Iterator, Mapping, Sequence
from types import TracebackType
from typing import ParamSpec, Self, TypeVar

from loguru import logger

from liblaf import grapes

from . import TimerRecords, get_time

_P = ParamSpec("_P")
_T = TypeVar("_T")


class timer(Mapping[str, float], contextlib.AbstractContextManager):  # noqa: N801
    counters: Sequence[str]
    depth: int = 0
    label: str | None = None
    records: TimerRecords
    record_log_level: int | str | None = "DEBUG"
    report_log_level: int | str | None = "INFO"
    _start: dict[str, float]
    _end: dict[str, float]

    def __init__(
        self,
        label: str | None = None,
        *,
        counters: Sequence[str] = ["perf", "process"],
        record_log_level: int | str | None = "DEBUG",
        report_at_exit: bool = False,
        report_log_level: int | str | None = "INFO",
    ) -> None:
        self.label = label
        self.counters = counters
        self.record_log_level = record_log_level
        self.report_log_level = report_log_level
        self.records = TimerRecords()
        self._start = {}
        self._end = {}
        if report_at_exit:
            TIMERS.append(self)

    def __getitem__(self, key: str) -> float:
        return self._end[key] - self._start[key]

    def __iter__(self) -> Iterator[str]:
        return iter(self.counters)

    def __len__(self) -> int:
        return len(self.counters)

    def __enter__(self) -> Self:
        if self.label is None:
            self.label = grapes.caller_location(2)
        self.depth += 1
        self.start()
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        self.end()
        self.depth -= 1

    def __call__(self, fn: Callable[_P, _T]) -> Callable[_P, _T]:
        if self.label is None:
            self.label = grapes.full_qual_name(fn)

        @functools.wraps(fn)
        def wrapped(*args: _P.args, **kwargs: _P.kwargs) -> _T:
            self.depth += 1
            with self:
                ret: _T = fn(*args, **kwargs)
            self.depth -= 1
            return ret

        return wrapped

    @property
    def elapsed(self) -> float:
        return self[self.counters[0]]

    def end(self) -> None:
        for name in self.counters:
            self._end[name] = get_time(name)
        self.records.append(self)
        self.depth += 1
        self.log_record()
        self.depth -= 1

    def human_report(self) -> str:
        return self.records.human_report(self.label)

    def human_record(self) -> str:
        text: str = f"{self.label} > " if self.label else ""
        for k, v in self.items():
            human: str = grapes.human_duration(v)
            text += f"{k}: {human}, "
        text = text.removesuffix(", ")
        return text

    def log_record(self, depth: int = 1) -> None:
        if not self.record_log_level:
            return
        logger.opt(depth=self.depth + depth).log(
            self.record_log_level, self.human_record()
        )

    def log_report(self, depth: int = 1) -> None:
        if not self.report_log_level:
            return
        logger.opt(depth=depth).log(self.report_log_level, self.human_report())

    def start(self) -> None:
        for name in self.counters:
            self._start[name] = get_time(name)

    def track(self, iterable: Iterable[_T], *, log_report: bool = True) -> Iterable[_T]:
        self.depth += 1
        if self.label is None:
            self.label = grapes.caller_location(2)
        for item in iterable:
            with self:
                yield item
        if log_report:
            self.log_report(self.depth + 1)
        self.depth -= 1


TIMERS: list[timer] = []


def exit_hook() -> None:
    for timer in TIMERS:
        if timer.records.count <= 1:
            continue
        timer.log_report()


atexit.register(exit_hook)
