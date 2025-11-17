import logging


def clear_children_stream_handlers(logger: str | logging.Logger | None = None) -> None:
    if logger is None or isinstance(logger, str):
        logger = logging.getLogger(logger)
    for child in logger.getChildren():
        for handler in child.handlers[:]:
            if isinstance(handler, logging.StreamHandler):
                child.removeHandler(handler)
        child.propagate = True
        clear_children_stream_handlers(child)
