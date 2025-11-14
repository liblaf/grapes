from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from .filters import new_filter
from .handler import RichHandler
from .helpers import init_levels

if TYPE_CHECKING:
    from .filters import FilterLike


def init(*, filter: FilterLike | None = None) -> None:  # noqa: A002
    init_levels()
    logging.basicConfig(handlers=[RichHandler()], level=logging.NOTSET)
    root: logging.Logger = logging.getLogger()
    root.addFilter(new_filter(filter))
