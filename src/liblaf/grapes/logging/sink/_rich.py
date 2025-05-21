import datetime
import types
from collections.abc import Sequence
from typing import Protocol, override

import attrs
import loguru
from rich.console import Console, RenderableType
from rich.highlighter import Highlighter, ReprHighlighter
from rich.table import Column, Table
from rich.text import Text
from rich.traceback import Traceback

from liblaf.grapes import pretty


class RichLoggingColumn(Protocol):
    @property
    def column(self) -> Column: ...
    def render(self, record: "loguru.Record") -> RenderableType: ...


@attrs.define
class LoguruRichHandler:
    console: Console = attrs.field(factory=lambda: pretty.get_console("stderr"))
    columns: Sequence[RichLoggingColumn] = attrs.field(
        factory=lambda: [TimeColumn(), LevelColumn(), LocationColumn(), MessageColumn()]
    )

    def __call__(self, message: "loguru.Message") -> None:
        record: loguru.Record = message.record
        # TODO: `console.print()` is slow
        self.console.print(self.render(record))
        if (excpetion := self.render_exception(record)) is not None:
            self.console.print(excpetion)

    def render(self, record: "loguru.Record") -> RenderableType:
        table: Table = Table.grid(
            *(col.column for col in self.columns), padding=(0, 1), expand=True
        )
        table.add_row(*(column.render(record) for column in self.columns))
        return table

    def render_exception(self, record: "loguru.Record") -> RenderableType | None:
        exception: loguru.RecordException | None = record["exception"]
        if exception is None:
            return None
        exc_type: type[BaseException] | None
        exc_value: BaseException | None
        traceback: types.TracebackType | None
        exc_type, exc_value, traceback = exception
        if exc_type is None or exc_value is None:
            return None
        return Traceback.from_exception(
            exc_type=exc_type,
            exc_value=exc_value,
            traceback=traceback,
            width=self.console.width,
            code_width=self.console.width,
            show_locals=True,
        )


class TimeColumn(RichLoggingColumn):
    @property
    @override
    def column(self) -> Column:
        return Column("Time", style="log.time")

    @override
    def render(self, record: "loguru.Record") -> RenderableType:
        elapsed: datetime.timedelta = record["elapsed"]
        hh: int
        mm: int
        ss: int
        mm, ss = divmod(int(elapsed.total_seconds()), 60)
        hh, mm = divmod(mm, 60)
        return f"{hh:02d}:{mm:02d}:{ss:02d}.{elapsed.microseconds:06d}"


@attrs.define
class LevelColumn(RichLoggingColumn):
    @property
    @override
    def column(self) -> Column:
        return Column("Level", style="log.level", width=8)

    @override
    def render(self, record: "loguru.Record") -> RenderableType:
        level: str = record["level"].name
        return Text(level, style=f"logging.level.{level.lower()}")


@attrs.define
class LocationColumn(RichLoggingColumn):
    enable_link: bool = attrs.field(default=True)

    @property
    @override
    def column(self) -> Column:
        return Column("Location", style="log.path")

    @override
    def render(self, record: "loguru.Record") -> RenderableType:
        location: Text = pretty.location(
            name=record["name"],
            function=record["function"],
            line=record["line"],
            file=record["file"].path,
            enable_link=self.enable_link,
        )
        return location


@attrs.define
class MessageColumn(RichLoggingColumn):
    highlighter: Highlighter = attrs.field(factory=ReprHighlighter)

    @property
    @override
    def column(self) -> Column:
        return Column("Message", style="log.message", ratio=1)

    @override
    def render(self, record: "loguru.Record") -> RenderableType:
        if (rich := record["extra"].get("rich")) is not None:
            return rich
        message: RenderableType = record["message"].rstrip()
        if record["extra"].get("markup", True):
            message = Text.from_markup(message)
        if highlighter := record["extra"].get("highlighter", self.highlighter):
            message = highlighter(message)
        return message
