import io

from rich.console import Console

from liblaf.grapes.rich.traceback import RichExceptionSummary


def test_rich_traceback() -> None:
    console = Console(file=io.StringIO())
    try:
        raise ValueError  # noqa: TRY301
    except ValueError as exc:
        exception = RichExceptionSummary(
            exc_type=type(exc), exc_value=exc, traceback=exc.__traceback__
        )
    with console.capture() as capture:
        console.print(exception)
    assert "ValueError" in capture.get()
