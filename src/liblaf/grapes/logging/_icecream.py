from loguru import logger

from liblaf import grapes


def init_icecream() -> None:
    if not grapes.has_module("icecream"):
        logger.warning(
            "`icecream` is not available. Skipping initialization of `icecream`."
        )
        return
    from icecream import ic

    ic.configureOutput(prefix="", outputFunction=icecream_output_function)


def icecream_output_function(s: str) -> None:
    logger.opt(depth=2).log("ICECREAM", s)
