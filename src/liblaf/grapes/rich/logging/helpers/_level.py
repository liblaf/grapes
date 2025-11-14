import logging
from collections.abc import Mapping

_DEFAULT_LEVELS: dict[int, str] = {5: "TRACE", 15: "ICECREAM", 25: "SUCCESS"}


def init_levels(levels: Mapping[int, str] | None = None) -> None:
    if levels is None:
        levels = _DEFAULT_LEVELS
    for level, name in levels.items():
        logging.addLevelName(level, name)
