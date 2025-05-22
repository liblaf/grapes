from loguru import logger

from liblaf import grapes


def main() -> None:
    grapes.init_logging()
    logger.success("Hello, {}!", "world")
    logger.info("super long message" * 100)

    try:
        msg: str = "TEST ERROR!"
        raise ValueError(msg)  # noqa: TRY301
    except ValueError:
        logger.exception("Exception:")


if __name__ == "__main__":
    main()
