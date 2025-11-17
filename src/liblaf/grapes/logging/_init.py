from __future__ import annotations

import logging
import os
from typing import TYPE_CHECKING

from liblaf.grapes._config import config
from liblaf.grapes.rich.logging import RichHandler

from .filters import FilterLike, as_filter
from .handlers import RichFileHandler
from .helpers import (
    HandlerRestrictedLogger,
    clear_children_stream_handlers,
    init_levels,
    install_excepthook,
    install_unraisablehook,
)

if TYPE_CHECKING:
    from logging import _FilterType


def init(
    *,
    file: str | os.PathLike[str] | None = None,
    filter: FilterLike | None = None,  # noqa: A002
    force: bool = False,
) -> None:
    if file is None:
        file = config.logging.file.get()
    init_levels()
    filter_: _FilterType = as_filter(filter)
    handlers: list[logging.Handler] = [RichHandler()]
    if file is not None:
        handlers.append(RichFileHandler(file))
    for handler in handlers:
        handler.addFilter(filter_)
    clear_children_stream_handlers()
    install_excepthook()
    install_unraisablehook()
    logging.basicConfig(level=logging.NOTSET, handlers=handlers, force=force)
    logging.setLoggerClass(HandlerRestrictedLogger)
