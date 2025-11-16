from __future__ import annotations

import logging
import os
from pathlib import Path
from typing import TYPE_CHECKING

from liblaf.grapes._config import config
from liblaf.grapes.rich import get_console
from liblaf.grapes.rich.logging import RichHandler

from .filters import FilterLike, as_filter
from .helpers import init_levels, install_excepthook, install_unraisablehook

if TYPE_CHECKING:
    from logging import _FilterType


def init(
    *,
    filter: FilterLike | None = None,  # noqa: A002
    file: str | os.PathLike[str] | None = None,
) -> None:
    if file is None:
        file = config.logging.file.get()
    init_levels()
    filter_: _FilterType = as_filter(filter)
    handlers: list[logging.Handler] = [RichHandler()]
    if file is not None:
        file = Path(file)
        handlers.append(RichHandler(console=get_console(file=file.open("w"))))
    for handler in handlers:
        handler.addFilter(filter_)
    logging.basicConfig(handlers=handlers, level=logging.NOTSET)
    install_excepthook()
    install_unraisablehook()
