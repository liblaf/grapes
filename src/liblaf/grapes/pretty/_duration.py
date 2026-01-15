from collections.abc import Iterable

from ._quantiphy import PrettyQuantitiesComponents, pretty_quantities, pretty_quantity


def pretty_duration(seconds: float, *, prec: int = 2, **kwargs) -> str:
    return pretty_quantity(seconds, "s", prec=prec, **kwargs)


def pretty_durations(
    seconds: Iterable[float], *, prec: int = 2, **kwargs
) -> PrettyQuantitiesComponents:
    return pretty_quantities(seconds, "s", prec=prec, **kwargs)
