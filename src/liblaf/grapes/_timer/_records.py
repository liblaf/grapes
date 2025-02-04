import collections
import textwrap
from collections.abc import Iterable, Mapping, Sequence

from liblaf import grapes

with grapes.optional_imports(extra="timer"):
    import numpy as np
    import polars as pl


class TimerRecords:
    _default_key: str = "perf"
    _records: dict[str, list[float]]

    def __init__(self, default_key: str = "perf") -> None:
        self._default_key = default_key
        self._records = collections.defaultdict(list)

    @property
    def count(self) -> int:
        return len(self.column())

    def append(
        self,
        seconds: float | Mapping[str, float] = {},
        nanoseconds: float | Mapping[str, float] = {},
    ) -> None:
        if not isinstance(seconds, Mapping):
            seconds = {self._default_key: seconds}
        if not isinstance(nanoseconds, Mapping):
            nanoseconds = {self._default_key: nanoseconds}
        for k, v in seconds.items():
            self._records[k].append(v)
        for k, v in nanoseconds.items():
            self._records[k].append(v * 1e-9)

    def column(self, key: str | None = None) -> Sequence[float]:
        return self._records[key or self._default_key]

    def human_report(self, label: str | None = None) -> str:
        label = label or "Timer"
        text: str = ""
        for k in self.keys():
            text += f"{k} > "
            arr: np.ndarray = self.to_numpy(k)
            human_mean: str = grapes.human_duration_series(arr)
            human_best: str = grapes.human_duration(arr.min())
            text += f"mean: {human_mean}, best: {human_best}\n"
        text = text.strip()
        text = f"{label} (total: {self.count})\n" + textwrap.indent(text, "  ")
        return text

    def keys(self) -> Iterable[str]:
        return self._records.keys()

    def row(self, index: int) -> dict[str, float]:
        return {k: v[index] for k, v in self._records.items()}

    def to_numpy(self, key: str | None = None) -> np.ndarray:
        return np.asarray(self.column(key))

    def to_polars(self) -> pl.DataFrame:
        return pl.from_dict(self._records)
