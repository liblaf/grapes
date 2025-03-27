import logging
import sys
import time

import pytest
from pytest_codspeed import BenchmarkFixture
from rich.console import Console
from rich.logging import RichHandler


@pytest.mark.benchmark(group="logging", timer=time.process_time, warmup=True)
def test_logging(benchmark: BenchmarkFixture) -> None:
    logging.basicConfig(stream=sys.stderr, force=True)
    logger: logging.Logger = logging.getLogger(__name__)
    benchmark(logger.info, "Hello, world!")


@pytest.mark.benchmark(group="logging", timer=time.process_time, warmup=True)
def test_logging_rich(benchmark: BenchmarkFixture) -> None:
    logging.basicConfig(
        format="%(message)s",
        datefmt="[%x]",
        handlers=[
            RichHandler(
                console=Console(force_terminal=True, stderr=True),
                omit_repeated_times=False,
            )
        ],
        force=True,
    )
    logger: logging.Logger = logging.getLogger(__name__)
    benchmark(logger.info, "Hello, world!")


@pytest.mark.benchmark(group="logging", timer=time.process_time, warmup=True)
def test_logging_rich_record(benchmark: BenchmarkFixture) -> None:
    logging.basicConfig(
        format="%(message)s",
        datefmt="[%x]",
        handlers=[
            RichHandler(
                console=Console(force_terminal=True, stderr=True, record=True),
                omit_repeated_times=False,
            )
        ],
        force=True,
    )
    logger: logging.Logger = logging.getLogger(__name__)
    benchmark(logger.info, "Hello, world!")
