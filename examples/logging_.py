from loguru import logger

from liblaf import grapes


def main() -> None:
    grapes.logging.init(profile="cherries")
    logger.success("Hello, {}!", "world")
    logger.info("long " * 100 + "message")

    try:
        msg: str = "Test Error!"
        raise ValueError(msg)  # noqa: TRY301
    except ValueError:
        logger.exception("Exception:")


if __name__ == "__main__":
    main()
