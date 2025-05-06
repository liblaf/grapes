from loguru import logger

from liblaf import grapes


def main() -> None:
    grapes.init_logging()
    logger.success("Hello, {}!", "world")


if __name__ == "__main__":
    main()
