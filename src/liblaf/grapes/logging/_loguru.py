import logging
from collections.abc import Sequence

import loguru
from environs import Env
from loguru import logger
from rich.logging import RichHandler

from liblaf import grapes


def init_logging(
    level: int | str = logging.NOTSET,
    handlers: Sequence[loguru.HandlerConfig] | None = None,
    levels: Sequence[loguru.LevelConfig] | None = None,
) -> None:
    if handlers is None:
        handlers: list[loguru.HandlerConfig] = [
            {
                "sink": RichHandler(console=grapes.logging.logging_console()),
                "format": "{message}",
            }
        ]
        env: Env = grapes.environ.init_env()
        if fpath := env.path("LOGGING_FILE", None):
            handlers.append({"sink": fpath, "mode": "w"})
        if fpath := env.path("LOGGING_JSONL", None):
            handlers.append({"sink": fpath, "serialize": True, "mode": "w"})
    if levels is None:
        levels = [
            {"name": "ICECREAM", "no": 15, "color": "<magenta><bold>", "icon": "🍦"}
        ]
    logger.configure(handlers=handlers, levels=levels)
    grapes.logging.setup_loguru_logging_intercept(level=level)
