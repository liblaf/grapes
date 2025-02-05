import atexit
import contextlib
import functools
from collections.abc import Callable, Generator, Iterable, Iterator, Mapping, Sequence
from types import TracebackType
from typing import ParamSpec, Self, TypeVar

import attrs
from loguru import logger

from liblaf import grapes

from . import TimerRecords, get_time

_P = ParamSpec("_P")
_T = TypeVar("_T")


@attrs.define
class timer(Mapping[str, float], contextlib.AbstractContextManager):  # noqa: N801
    """A class for measuring and recording execution time using various counters.

    This class provides a context manager and decorator for timing code execution. It supports multiple counters, logging, and generating human-readable reports of the recorded timings.

    Example: Using `timer` as a context manager
        ```python
        with timer():
            # Code to be timed
            time.sleep(1)
        ```

    Example: Using `timer` as a decorator
        ```python
        @timer(report_at_exit=True)
        def example_function():
            # Code to be timed
            time.sleep(1)


        example_function()
        ```

    Example: Tracking an iterable with `timer`
        ```python
        items = [1, 2, 3]
        for item in timer().track(items):
            # Code to be timed for each item
            time.sleep(1)
        ```
    """

    counters: Sequence[str] = ["perf", "process"]
    depth: int = 0
    label: str | None = None
    record_log_level: int | str | None = "DEBUG"
    records: TimerRecords = attrs.field(factory=TimerRecords, init=False)
    report_at_exit: bool = False
    report_log_level: int | str | None = "INFO"
    _end: dict[str, float] = attrs.field(factory=dict, init=False)
    _start: dict[str, float] = attrs.field(factory=dict, init=False)

    def __attrs_post_init__(self) -> None:
        """Post-initialization method for the class.

        This method is automatically called after the class is initialized. If the `report_at_exit` attribute is set to True, the instance is added to the global `TIMERS` list.
        """
        if self.report_at_exit:
            TIMERS.append(self)

    def __getitem__(self, key: str) -> float:
        """Retrieve the elapsed time for a given key.

        Args:
            key: The key for which to retrieve the elapsed time.

        Returns:
            The elapsed time corresponding to the given key.
        """
        return self._end[key] - self._start[key]

    def __iter__(self) -> Iterator[str]:
        """Returns an iterator over the counters.

        Yields:
            An iterator over the string representations of the counters.
        """
        return iter(self.counters)

    def __len__(self) -> int:
        """Return the number of counters.

        Returns:
            The number of counters in the collection.
        """
        return len(self.counters)

    def __enter__(self) -> Self:
        """Enter the runtime context related to this object.

        This method is called when execution flow enters the context of the `with` statement. It initializes the timer by setting the label if it is not already set, increments the depth counter, and starts the timer.

        Returns:
            The instance of the timer object.
        """
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
        """Exit the runtime context related to this object.

        This method is called when the execution leaves the context of the `with` statement that this object is used in. It ensures that the timer is stopped and the depth counter is decremented.

        Args:
            exc_type: The exception type if an exception was raised, otherwise None.
            exc_value: The exception instance if an exception was raised, otherwise None.
            traceback: The traceback object if an exception was raised, otherwise None.
        """
        self.end()
        self.depth -= 1

    def __call__(self, fn: Callable[_P, _T]) -> Callable[_P, _T]:
        """A decorator that wraps a function to measure its execution time.

        Args:
            fn: The function to be wrapped.

        Returns:
            The wrapped function with timing functionality.
        """
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
        """The elapsed time for the first counter."""
        return self[self.counters[0]]

    def end(self) -> None:
        """Ends the timing for all counters, records the end times, and logs the record.

        This method performs the following actions:
        1. Iterates over all counter names and records their end times using `get_time`.
        2. Appends the current instance to the records list.
        3. Increments the depth counter.
        4. Logs the current record.
        5. Decrements the depth counter.
        """
        for name in self.counters:
            self._end[name] = get_time(name)
        self.records.append(self)
        self.depth += 1
        self.log_record()
        self.depth -= 1

    def human_report(self) -> str:
        """Generates a human-readable report of the recorded timings.

        Returns:
            A string containing the human-readable report of the timings.
        """
        return self.records.human_report(self.label)

    def human_record(self) -> str:
        """Generate a human-readable string representation of the recorded durations.

        This method iterates over the items in the instance, converts each duration to a human-readable format using `grapes.human_duration`, and constructs a formatted string. If a label is present, it is included at the beginning of the string.

        Returns:
            A human-readable string representation of the recorded durations.
        """
        text: str = f"{self.label} > " if self.label else ""
        for k, v in self.items():
            human: str = grapes.human_duration(v)
            text += f"{k}: {human}, "
        text = text.removesuffix(", ")
        return text

    def log_record(self, depth: int = 1) -> None:
        """Logs a record if the record_log_level is set.

        Args:
            depth: The depth to be added to the current depth for logging.
        """
        if not self.record_log_level:
            return
        logger.opt(depth=self.depth + depth).log(
            self.record_log_level, self.human_record()
        )

    def log_report(self, depth: int = 1) -> None:
        """Logs a human-readable report at the specified log level.

        Args:
            depth: The stack depth to use for the log entry.
        """
        if not self.report_log_level:
            return
        logger.opt(depth=depth).log(self.report_log_level, self.human_report())

    def start(self) -> None:
        """Starts the timer for each counter in the `counters` list.

        This method iterates over the `counters` list and initializes the corresponding start time for each counter using the `get_time` function.
        """
        for name in self.counters:
            self._start[name] = get_time(name)

    def track(
        self, iterable: Iterable[_T], *, log_report: bool = True
    ) -> Generator[_T]:
        """Tracks the execution time of an iterable's items.

        Args:
            iterable: The iterable to be tracked.
            log_report: If `True`, logs the report after tracking.

        Yields:
            The items of the input iterable, one by one.
        """
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
