from __future__ import annotations

import logging
import os
from pathlib import Path
from typing import TYPE_CHECKING

from liblaf.grapes._config import config
from liblaf.grapes.rich import get_console
from liblaf.grapes.rich.logging import RichHandler

from .filters import FilterLike, as_filter
from .helpers import (
    clear_children_handlers,
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
    root: logging.Logger = logging.getLogger()
    if not force and root.hasHandlers():
        return
    if file is None:
        file = config.logging.file.get()
    init_levels()
    filter_: _FilterType = as_filter(filter)
    handlers: list[logging.Handler] = [RichHandler()]
    if file is not None:
        file = Path(file)
        file.parent.mkdir(parents=True, exist_ok=True)
        handlers.append(RichHandler(console=get_console(file=file.open("w"))))
    for handler in handlers:
        handler.addFilter(filter_)
    logging.basicConfig(level=logging.NOTSET, handlers=handlers, force=force)
    install_excepthook()
    install_unraisablehook()
    clear_children_handlers()
