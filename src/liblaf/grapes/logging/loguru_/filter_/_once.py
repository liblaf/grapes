import operator
from collections.abc import Sequence

import loguru

DEFAULT_KEYS: Sequence[str] = (
    "file",
    "function",
    "level",
    "line",
    "message",
    "module",
    "name",
)


def filter_once(keys: Sequence[str] = DEFAULT_KEYS) -> loguru.FilterFunction:
    history: set[tuple] = set()
    transform = operator.itemgetter(*keys)

    def filter_(record: loguru.Record) -> bool:
        partial: tuple = transform(record)
        if partial in history:
            return False
        history.add(partial)
        return True

    return filter_
