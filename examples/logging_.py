from loguru import logger

from liblaf import grapes


def main() -> None:
    grapes.logging.init()
    logger.trace("This is a trace message.")
    logger.debug("This is a debug message.")
    ic("This is an icecream message.")
    logger.info("This is an info message.")
    logger.success("This is a success message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")
    logger.info("long " * 100 + "message")

    try:
        msg: str = "Test Error!"
        raise ValueError(msg)  # noqa: TRY301
    except ValueError:
        logger.exception("Exception:")


if __name__ == "__main__":
    main()
