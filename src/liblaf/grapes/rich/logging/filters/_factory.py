from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING

from ._composite import CompositeFilter

if TYPE_CHECKING:
    from logging import _FilterType

    type FilterLike = _FilterType | Mapping[str, int | str]


def new_filter(f: FilterLike | None = None, /) -> _FilterType:
    if f is None:
        return CompositeFilter()
    if isinstance(f, Mapping):
        return CompositeFilter(f)
    return f
