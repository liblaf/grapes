import math
from collections.abc import Sequence
from typing import NamedTuple


class Spec(NamedTuple):
    multiplier: float
    threshold: float
    unit: str


SPECS: Sequence[Spec] = (
    Spec(1e9, 1e3, "ns"),
    Spec(1e6, 1e3, "µs"),
    Spec(1e3, 1e3, "ms"),
    Spec(1, 1e2, "s"),
)


def auto_resolution(seconds: float, *, sig: int = 3) -> int:
    for resolution in range(10, -3, -1):
        number: float = seconds * 10**resolution
        number = round(number, sig)
        if number < 10:
            return resolution
    seconds = round(seconds)
    days: int
    days, seconds = divmod(seconds, 24 * 60 * 60)
    if days > 0:
        return -4
    hours: int
    hours, seconds = divmod(seconds, 60 * 60)
    if hours > 0:
        return -3
    minutes: int
    minutes, seconds = divmod(seconds, 60)
    if minutes > 0:
        return -2
    return 0


def pretty_duration(
    seconds: float, *, sig: int = 3, resolution: int | None = None
) -> str:
    """.

    Examples:
        >>> pretty_duration(math.nan)
        '?? s'
        >>> pretty_duration(1e-13)
        '.000 ns'
        >>> pretty_duration(1e-12)
        '.001 ns'
        >>> pretty_duration(1e-11)
        '.010 ns'
        >>> pretty_duration(1e-10)
        '.100 ns'
        >>> pretty_duration(1e-9)
        '1.00 ns'
        >>> pretty_duration(1e-8)
        '10.0 ns'
        >>> pretty_duration(1e-7)
        '100. ns'
        >>> pretty_duration(1e-6)
        '1.00 µs'
        >>> pretty_duration(1e-5)
        '10.0 µs'
        >>> pretty_duration(1e-4)
        '100. µs'
        >>> pretty_duration(1e-3)
        '1.00 ms'
        >>> pretty_duration(1e-2)
        '10.0 ms'
        >>> pretty_duration(1e-1)
        '100. ms'
        >>> pretty_duration(1.0)
        '1.00 s'
        >>> pretty_duration(1e1)
        '10.0 s'
        >>> pretty_duration(1e2)
        '01:40'
        >>> pretty_duration(1e3)
        '16:40'
        >>> pretty_duration(1e4)
        '02:46:40'
        >>> pretty_duration(1e5)
        '1d,03:46:40'
        >>> pretty_duration(1e6)
        '11d,13:46:40'
    """
    if not math.isfinite(seconds):
        return "?? s"
    if resolution is None:
        resolution = auto_resolution(seconds, sig=sig)
    resolution = max(min(resolution, 10), -4)
    for multiplier, threshold, unit in SPECS:
        if 10**-resolution < threshold / multiplier:
            number: float = seconds * multiplier
            precision: int = resolution + sig - round(math.log10(multiplier)) - 1
            width: int = sig + 1
            number_str: str = f"{number:#0{width}.{precision}f}"
            if width == precision + 1:
                number_str = number_str.removeprefix("0")
            return f"{number_str} {unit}"
    seconds = round(seconds)
    match resolution:
        case -2:
            minutes: int
            minutes, seconds = divmod(seconds, 60)
            return f"{minutes:02d}:{seconds:02d}"
        case -3:
            hours: int
            minutes: int
            hours, seconds = divmod(seconds, 60 * 60)
            minutes, seconds = divmod(seconds, 60)
            return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        case -4:
            days: int
            hours: int
            days, seconds = divmod(seconds, 24 * 60 * 60)
            hours, seconds = divmod(seconds, 60 * 60)
            minutes, seconds = divmod(seconds, 60)
            return f"{days}d,{hours:02d}:{minutes:02d}:{seconds:02d}"
    return f"{seconds} s"
