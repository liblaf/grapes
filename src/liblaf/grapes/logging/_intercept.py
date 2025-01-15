import inspect
import itertools
import logging
from collections.abc import Iterable

from loguru import logger


class InterceptHandler(logging.Handler):
    """Intercept standard logging messages toward Loguru sinks.

    References:
        [1] [Overview — loguru documentation](https://loguru.readthedocs.io/en/stable/overview.html#entirely-compatible-with-standard-logging)
    """

    def emit(self, record: logging.LogRecord) -> None:
        # Get corresponding Loguru level if it exists.
        level: str | int
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message.
        frame, depth = inspect.currentframe(), 0
        while frame and (depth == 0 or frame.f_code.co_filename == logging.__file__):
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )


def setup_loguru_logging_intercept(
    level: int | str = logging.NOTSET, modules: Iterable[str] = ()
) -> None:
    """...

    References:
        [1] [loguru-logging-intercept/loguru_logging_intercept.py at f358b75ef4162ea903bf7a3298c22b1be83110da · MatthewScholefield/loguru-logging-intercept](https://github.com/MatthewScholefield/loguru-logging-intercept/blob/f358b75ef4162ea903bf7a3298c22b1be83110da/loguru_logging_intercept.py#L35C5-L42)
    """
    logging.basicConfig(level=level, handlers=[InterceptHandler()])
    for logger_name in itertools.chain(("",), modules):
        mod_logger: logging.Logger = logging.getLogger(logger_name)
        mod_logger.handlers = [InterceptHandler(level=level)]
        mod_logger.propagate = False
