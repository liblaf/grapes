from collections.abc import Generator, Iterable
from typing import Any, TypeVar

from rich.console import RenderableType
from rich.progress import (
    BarColumn,
    MofNCompleteColumn,
    Progress,
    ProgressColumn,
    SpinnerColumn,
    Task,
    TaskProgressColumn,
    TextColumn,
    TimeElapsedColumn,
    TimeRemainingColumn,
)
from rich.table import Column
from rich.text import Text

from liblaf import grapes


class RateColumn(ProgressColumn):
    unit: str = "it"

    def __init__(self, unit: str = "it", table_column: Column | None = None) -> None:
        super().__init__(table_column)
        self.unit = unit

    def render(self, task: Task) -> RenderableType:
        if not task.speed:
            return Text(f"?{self.unit}/s", style="progress.data.speed")
        human: str = grapes.human_throughout(task.speed, self.unit)
        return Text(human, style="progress.data.speed")


_T = TypeVar("_T")


def track(
    sequence: Iterable[_T], description: str | None = "Working..."
) -> Generator[_T, Any, None]:
    columns: list[ProgressColumn] = [SpinnerColumn()]
    if description:
        columns.append(TextColumn("[progress.description]{task.description}"))
    columns += [
        BarColumn(),
        TaskProgressColumn(show_speed=True),
        MofNCompleteColumn(),
        "[",
        TimeElapsedColumn(),
        "<",
        TimeRemainingColumn(),
        ",",
        RateColumn(),
        "]",
    ]
    with Progress(*columns, console=grapes.logging_console()) as progress:
        yield from progress.track(sequence, description=description or "")
