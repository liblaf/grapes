import logging

from liblaf.grapes.rich.logging import RichHandler

from .filters import FilterLike, as_filter
from .helpers import init_levels, install_excepthook, install_unraisablehook


def init(*, filter: FilterLike | None = None) -> None:  # noqa: A002
    init_levels()
    handler = RichHandler()
    handler.addFilter(as_filter(filter))
    logging.basicConfig(handlers=[handler], level=logging.NOTSET)
    install_excepthook()
    install_unraisablehook()
