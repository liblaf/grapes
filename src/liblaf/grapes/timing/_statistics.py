import math
import statistics
from collections.abc import Sequence

import autoregistry

from liblaf.grapes import pretty

type StatisticName = str


STATISTICS_REGISTRY = autoregistry.Registry(prefix="_compute_")


STATISTICS_REGISTRY["max"] = max
STATISTICS_REGISTRY["mean"] = statistics.mean
STATISTICS_REGISTRY["median"] = statistics.median
STATISTICS_REGISTRY["min"] = min
STATISTICS_REGISTRY["stdev"] = statistics.stdev
STATISTICS_REGISTRY["total"] = sum


def compute_statistic(series: Sequence[float], stat_name: StatisticName) -> float:
    try:
        return STATISTICS_REGISTRY[stat_name](series)
    except (ValueError, statistics.StatisticsError):
        return math.nan


def pretty_statistic(
    series: Sequence[float], stat_name: StatisticName
) -> tuple[str, str]:
    match stat_name:
        case "mean+stdev":
            mean: float = compute_statistic(series, "mean")
            stdev: float = compute_statistic(series, "stdev")
            pretty_name: str = "mean ± σ"  # noqa: RUF001
            pretty_value: str = pretty.pretty_durations((mean, stdev), sep=" ± ")
            return pretty_name, pretty_value
        case "range":
            minimum: float = compute_statistic(series, "min")
            maximum: float = compute_statistic(series, "max")
            pretty_name: str = "min … max"
            pretty_value: str = pretty.pretty_durations((minimum, maximum), sep=" … ")
            return pretty_name, pretty_value
        case stat_name:
            value: float = compute_statistic(series, stat_name)
            return stat_name, pretty.pretty_duration(value)
