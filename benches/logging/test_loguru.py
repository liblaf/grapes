import functools

import loguru
import pytest
from loguru import logger
from pytest_codspeed import BenchmarkFixture
from rich.console import Console
from rich.logging import RichHandler


@pytest.mark.benchmark(group="logging", warmup=True)
def test_loguru(benchmark: BenchmarkFixture) -> None:
    logger.configure()
    benchmark(logger.info, "Hello, world!")


@pytest.mark.benchmark(group="logging", warmup=True)
def test_loguru_rich_handler(benchmark: BenchmarkFixture) -> None:
    logger.configure(
        handlers=[
            {
                "sink": RichHandler(
                    console=Console(force_terminal=True, stderr=True),
                    omit_repeated_times=False,
                ),
                "format": "{message}",
            }
        ]
    )
    benchmark(logger.info, "Hello, world!")


@pytest.mark.benchmark(group="logging", warmup=True)
def test_loguru_rich_handler_record(benchmark: BenchmarkFixture) -> None:
    logger.configure(
        handlers=[
            {
                "sink": RichHandler(
                    console=Console(force_terminal=True, stderr=True, record=True),
                    omit_repeated_times=False,
                ),
                "format": "{message}",
            }
        ]
    )
    benchmark(logger.info, "Hello, world!")


def loguru_rich_console(message: "loguru.Message", console: Console) -> None:
    console.print(message, end="")


@pytest.mark.benchmark(group="logging", warmup=True)
def test_loguru_rich_console(benchmark: BenchmarkFixture) -> None:
    logger.configure(
        handlers=[
            {
                "sink": functools.partial(
                    loguru_rich_console,
                    console=Console(force_terminal=True, stderr=True),
                ),
                "format": "{message}",
            }
        ]
    )
    benchmark(logger.info, "Hello, world!")
