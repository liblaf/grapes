from collections.abc import Sequence
from pathlib import Path
from typing import Unpack

import loguru
from environs import env
from rich.console import Console

from liblaf.grapes import pretty
from liblaf.grapes.logging.filters import Filter, make_filter
from liblaf.grapes.logging.sink import (
    LevelColumn,
    LocationColumn,
    LoguruRichHandler,
    MessageColumn,
    RichLoggingColumn,
    TimeColumn,
)
from liblaf.grapes.typed import PathLike


def rich_handler(
    console: Console | None = None,
    columns: Sequence[RichLoggingColumn] | None = None,
    filter_: Filter | None = None,
    *,
    enable_link: bool = True,
    **kwargs: Unpack["loguru.BasicHandlerConfig"],
) -> "loguru.HandlerConfig":
    if console is None:
        console = pretty.get_console("stderr")
    if columns is None:
        columns = [
            TimeColumn(),
            LevelColumn(),
            LocationColumn(enable_link=enable_link),
            MessageColumn(),
        ]
    filter_ = make_filter(filter_)
    return {
        "sink": LoguruRichHandler(console=console, columns=columns),
        "format": "",
        "filter": filter_,
        **kwargs,
    }


def file_handler(
    file: PathLike | None = None,
    filter_: Filter | None = None,
    **kwargs: Unpack["loguru.BasicHandlerConfig"],
) -> "loguru.HandlerConfig":
    if file is None:
        file = env.path("LOGGING_FILE", default=Path("run.log"))
    console: Console = pretty.get_console(file)
    filter_ = make_filter(filter_)
    return {
        "sink": LoguruRichHandler(console=console),
        "format": "",
        "filter": filter_,
        **kwargs,
    }
