from __future__ import annotations

import logging
import sys

logger: logging.Logger = logging.getLogger()


def install_unraisablehook(level: int = logging.ERROR) -> None:
    def unraisablehook(args: sys.UnraisableHookArgs, /) -> None:
        if args.exc_value is None:
            return
        logger.log(
            level,
            "{err_msg}: {object!r}",
            exc_info=(args.exc_type, args.exc_value, args.exc_traceback),
        )

    sys.unraisablehook = unraisablehook
