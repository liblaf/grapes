import itertools
import time

import joblib
from loguru import logger

from liblaf import grapes


def fun(x: float, exp: float) -> float:
    time.sleep(1)
    return x**exp


def main() -> None:
    grapes.logging.LoggingProfileDefault().init()
    joblib.parallel_config(n_jobs=-2, prefer="processes")
    for y in grapes.parallel(
        fun, range(20), itertools.repeat(2), return_as="generator"
    ):
        logger.info("y = {}", y)


if __name__ == "__main__":
    main()
