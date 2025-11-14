from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from liblaf.grapes.rich.logging import RichHandler

from .filters import as_filter
from .helpers import init_levels, install_excepthook, install_unraisablehook

if TYPE_CHECKING:
    from .filters import FilterLike


def init(*, filter: FilterLike | None = None) -> None:  # noqa: A002
    init_levels()
    logging.basicConfig(handlers=[RichHandler()], level=logging.NOTSET)
    root: logging.Logger = logging.getLogger()
    root.addFilter(as_filter(filter))
    install_excepthook()
    install_unraisablehook()
