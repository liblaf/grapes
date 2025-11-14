import logging
from collections.abc import Generator, Iterable

from rich.console import Console, RenderableType
from rich.text import Text

from liblaf.grapes.rich._get_console import get_console

from .columns import (
    RichHandlerColumn,
    RichHandlerColumnLevel,
    RichHandlerColumnLocation,
    RichHandlerColumnTime,
)


def _default_columns() -> list[RichHandlerColumn]:
    return [
        RichHandlerColumnTime(),
        RichHandlerColumnLevel(),
        RichHandlerColumnLocation(),
    ]


class RichHandler(logging.Handler):
    columns: list[RichHandlerColumn]
    console: Console
    time_relative: bool = True

    def __init__(
        self,
        /,
        *,
        columns: Iterable[RichHandlerColumn] | None = None,
        console: Console | None = None,
        level: int = logging.NOTSET,
    ) -> None:
        super().__init__(level=level)
        columns = _default_columns() if columns is None else list(columns)
        if console is None:
            console = get_console(stderr=True)
        self.columns = columns
        self.console = console

    def emit(self, record: logging.LogRecord) -> None:
        self.console.print(
            *self._render(record),
            sep="",
            end="",
            overflow="ignore",
            no_wrap=True,
            highlight=False,
            crop=False,
            soft_wrap=False,
        )

    def _render(self, record: logging.LogRecord) -> Generator[RenderableType]:
        columns: list[Text] = [column.render(record) for column in self.columns]
        meta: Text = Text(" ").join(columns) + Text(" ")
        message: str = record.getMessage()
        for line in message.splitlines():
            yield meta
            yield Text(line, "log.message")
            yield "\n"
