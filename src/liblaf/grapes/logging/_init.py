import logging
from collections.abc import Sequence

import loguru

from liblaf import grapes


def init_logging(
    level: int | str = logging.NOTSET,
    *,
    handlers: Sequence["loguru.HandlerConfig"] | None = None,
    levels: Sequence["loguru.LevelConfig"] | None = None,
    traceback_show_locals: bool = True,
) -> None:
    grapes.logging.init_rich(show_locals=traceback_show_locals)
    grapes.logging.init_loguru(level=level, handlers=handlers, levels=levels)
    grapes.logging.init_icecream()
