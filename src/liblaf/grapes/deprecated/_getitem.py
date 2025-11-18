from __future__ import annotations

from collections.abc import Iterable
from typing import TYPE_CHECKING

from liblaf.grapes.logging import depth_logger

if TYPE_CHECKING:
    from _typeshed import SupportsContainsAndGetItem


def getitem[KT, VT](
    mapping: SupportsContainsAndGetItem[KT, VT],
    key: KT,
    deprecated_keys: Iterable[KT] = (),
) -> object:
    if key in mapping:
        return mapping[key]
    for deprecated_key in deprecated_keys:
        if deprecated_key in mapping:
            depth_logger.warning(
                "'%s' is deprecated. Please use '%s' instead.",
                deprecated_key,
                key,
                stacklevel=2,
            )
            return mapping[deprecated_key]
    raise KeyError(key)
