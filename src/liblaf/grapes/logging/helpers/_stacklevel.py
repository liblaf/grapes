import inspect
import logging
import types
from typing import Any

from liblaf.grapes import magic

_PROXY_METHODS: set[str] = {
    "debug",
    "info",
    "warning",
    "error",
    "critical",
    "log",
    "exception",
    "findCaller",
}


class DepthLogger:
    def __getattr__(self, name: str) -> Any:
        if name in _PROXY_METHODS:

            def method(*args, **kwargs) -> None:
                depth: int = kwargs.get("stacklevel", 1)
                frame: types.FrameType | None = inspect.currentframe()
                stacklevel: int = 1
                while frame is not None and depth > 0:
                    frame = frame.f_back
                    depth -= 1
                    stacklevel += 1
                    while frame is not None and magic.hidden_from_logging(frame):
                        frame = frame.f_back
                        stacklevel += 1
                logger_name: str | None = None
                if frame is not None:
                    logger_name = frame.f_globals.get("__name__")
                logger: logging.Logger = logging.getLogger(logger_name)
                kwargs["stacklevel"] = stacklevel
                return getattr(logger, name)(*args, **kwargs)

            return method
        frame: types.FrameType | None = inspect.currentframe()
        if frame is not None:
            frame = frame.f_back
        logger_name: str | None = None
        if frame is not None:
            logger_name = frame.f_globals.get("__name__")
        logger: logging.Logger = logging.getLogger(logger_name)
        return getattr(logger, name)


depth_logger = DepthLogger()
