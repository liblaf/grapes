import logging

import pytest

from liblaf.grapes.logging import depth_logger

_MESSAGE: str = "message from wrapped"


def wrapped() -> None:
    depth_logger.info(_MESSAGE, stacklevel=2)


def wrapper() -> None:
    __tracebackhide__ = True
    wrapped()


def test_depth_logger(caplog: pytest.LogCaptureFixture) -> None:
    with caplog.at_level(logging.INFO, __name__):
        wrapper()
    assert len(caplog.records) == 1
    record: logging.LogRecord = caplog.records[0]
    assert record.funcName == "test_depth_logger"
    assert record.msg == _MESSAGE
