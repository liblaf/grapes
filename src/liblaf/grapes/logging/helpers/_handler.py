import logging
from typing import override

_ALLOWED_LOGGERS: set[str] = {"root"}


class HandlerRestrictedLogger(logging.Logger):
    @override
    def addHandler(self, hdlr: logging.Handler) -> None:
        if (
            isinstance(hdlr, logging.StreamHandler)
            and self.name not in _ALLOWED_LOGGERS
        ):
            return
        super().addHandler(hdlr)
