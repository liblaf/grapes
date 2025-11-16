import logging

from liblaf import grapes

logger: logging.Logger = logging.getLogger(__name__)


def main() -> None:
    grapes.logging.init()
    logger.log(5, "This is a trace message.")
    logger.debug("This is a debug message.")
    ic("This is an icecream message.")
    logger.info("This is an info message.")
    logger.log(25, "This is a success message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message!")
    logger.info("long " * 100 + "message")  # noqa: G003
    logger.info("Multiline message:\nLine 1\nLine 2\nLine 3")

    try:
        msg: str = "This is an exception!"
        raise ValueError(msg)  # noqa: TRY301
    except ValueError:
        logger.exception("")


if __name__ == "__main__":
    main()
