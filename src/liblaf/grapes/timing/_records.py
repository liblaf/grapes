import collections
import statistics
import textwrap
from collections.abc import Iterable, Mapping, Sequence

from liblaf import grapes


class TimerRecords:
    """A class to manage and store timer records with various functionalities."""

    _default_key: str = "perf"
    _records: dict[str, list[float]]

    def __init__(self, default_key: str = "perf") -> None:
        """Initializes the _records object with a default key.

        Args:
            default_key: The default key to be used for the records.
        """
        self._default_key = default_key
        self._records = collections.defaultdict(list)

    @property
    def count(self) -> int:
        """The number of elements in the column."""
        return len(self.column())

    def append(
        self,
        seconds: float | Mapping[str, float] = {},
        nanoseconds: float | Mapping[str, float] = {},
    ) -> None:
        """Append time records to the internal storage.

        Args:
            seconds: Time in seconds to be appended. If a float is provided, it will be stored with the default key. If a mapping is provided, it will be stored with the corresponding keys.
            nanoseconds: Time in nanoseconds to be appended. If a float is provided, it will be stored with the default key. If a mapping is provided, it will be stored with the corresponding keys. The values will be converted to seconds before storing.
        """
        if not isinstance(seconds, Mapping):
            seconds = {self._default_key: seconds}
        if not isinstance(nanoseconds, Mapping):
            nanoseconds = {self._default_key: nanoseconds}
        for k, v in seconds.items():
            self._records[k].append(v)
        for k, v in nanoseconds.items():
            self._records[k].append(v * 1e-9)

    def column(self, key: str | None = None) -> Sequence[float]:
        """Retrieve a sequence of float values from the records.

        Args:
            key: The key to retrieve the sequence of floats. If None, the default key is used.

        Returns:
            A sequence of float values corresponding to the given key.
        """
        return self._records[key or self._default_key]

    def human_report(self, label: str | None = None) -> str:
        """Generates a human-readable report of the timer records.

        Args:
            label: A label for the report. Defaults to "Timer".

        Returns:
            A formatted string containing the report with mean and best durations for each key.
        """
        label = label or "Timer"
        text: str = ""
        for k in self.keys():
            text += f"{k} > "
            human_mean: str = grapes.human_duration_series(self.column(k))
            human_best: str = grapes.human_duration(self.min(k))
            text += f"mean: {human_mean}, best: {human_best}\n"
        text = text.strip()
        text = f"{label} (total: {self.count})\n" + textwrap.indent(text, "  ")
        return text

    def keys(self) -> Iterable[str]:
        """Retrieve the keys from the records.

        Returns:
            An iterable containing the keys of the records.
        """
        return self._records.keys()

    def max(self, key: str | None = None) -> float:
        """Retrieve the maximum value from the specified column.

        Args:
            key: The key of the column to retrieve the maximum value. If None, the default column is used.

        Returns:
            The maximum value from the specified column.
        """
        return max(self.column(key))

    def mean(self, key: str | None = None) -> float:
        """Calculate the mean of the specified column.

        Args:
            key: The key of the column to calculate the mean. If None, the default column is used.

        Returns:
            The mean of the column.
        """
        return statistics.mean(self.column(key))

    def median(self, key: str | None = None) -> float:
        """Calculate the median of the specified column.

        Args:
            key: The key of the column to calculate the median. If None, the default column is used.

        Returns:
            The median of the column.
        """
        return statistics.median(self.column(key))

    def min(self, key: str | None = None) -> float:
        """Retrieve the minimum value from the specified column.

        Args:
            key: The key of the column to retrieve the minimum value. If None, the default column is used.

        Returns:
            The minimum value from the specified column.
        """
        return min(self.column(key))

    def row(self, index: int) -> dict[str, float]:
        """Retrieve a specific row from the records.

        Args:
            index: The index of the row to retrieve.

        Returns:
            A dictionary where the keys are the record names and the values are the corresponding values from the specified row.
        """
        return {k: v[index] for k, v in self._records.items()}

    def stdev(self, key: str | None = None) -> float:
        """Calculate the standard deviation of the specified column.

        Args:
            key: The key of the column to calculate the standard deviation. If None, the default column is used.

        Returns:
            The standard deviation of the column.
        """
        return statistics.stdev(self.column(key))
