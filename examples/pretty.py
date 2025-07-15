from loguru import logger

from liblaf import grapes


def fun(a: int, b: int) -> int:
    return a + b


def main() -> None:
    grapes.logging.init()
    logger.info(grapes.pretty_call(fun, args=(1, 2)))
    logger.info(grapes.pretty_call(fun, args=(1,), kwargs={"b": 2}))
    logger.info(grapes.pretty_call(fun, kwargs={"a": 1, "b": 2}))


if __name__ == "__main__":
    main()
