import enum
from pathlib import Path
from typing import override

import pydantic

from ._base import BaseModel
from ._paths import paths


class LogLevel(enum.StrEnum):
    """.

    References:
        1. <https://github.com/Delgan/loguru/blob/master/loguru/_defaults.py>
    """

    @override
    @staticmethod
    def _generate_next_value_(
        name: str, start: int, count: int, last_values: list[str]
    ) -> str:
        return name.upper()

    TRACE = enum.auto()
    DEBUG = enum.auto()
    INFO = enum.auto()
    SUCCESS = enum.auto()
    WARNING = enum.auto()
    ERROR = enum.auto()
    CRITICAL = enum.auto()


class ConfigLoggingTraceback(BaseModel):
    """.

    References:
        1. [`rich.traceback.Traceback.from_exception`](https://rich.readthedocs.io/en/stable/reference/traceback.html#rich.traceback.Traceback.from_exception)
    """

    width: int | None = pydantic.Field(default=None)
    """Number of characters used to traceback."""

    code_width: int | None = pydantic.Field(default=None)
    """Number of code characters used to traceback."""

    extra_lines: int = pydantic.Field(default=3)
    """Additional lines of code to render."""

    show_locals: int = pydantic.Field(default=True)
    """Enable display of local variables."""


class ConfigLogging(BaseModel):
    file: Path = pydantic.Field(default=paths.log_file)
    level: str | int = pydantic.Field(default="INFO")
    traceback: ConfigLoggingTraceback = pydantic.Field(
        default_factory=ConfigLoggingTraceback
    )
