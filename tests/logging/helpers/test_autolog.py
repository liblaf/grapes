import logging

import pytest

from liblaf.grapes.logging import autolog

_MESSAGE: str = "message from wrapped"


def wrapped() -> None:
    autolog.info(_MESSAGE, stacklevel=2)


def wrapper() -> None:
    _logging_hide = True
    wrapped()


def test_autolog(caplog: pytest.LogCaptureFixture) -> None:
    with caplog.at_level(logging.INFO, __name__):
        wrapper()
    assert len(caplog.records) == 1
    record: logging.LogRecord = caplog.records[0]
    assert record.funcName == "test_autolog"
    assert record.msg == _MESSAGE
