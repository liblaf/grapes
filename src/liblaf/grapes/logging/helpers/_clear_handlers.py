import logging


def clear_children_handlers(logger: str | logging.Logger | None = None) -> None:
    if logger is None or isinstance(logger, str):
        logger = logging.getLogger(logger)
    for child in logger.getChildren():
        child.handlers.clear()
        child.propagate = True
        clear_children_handlers(child)
