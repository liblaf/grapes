from pathlib import Path

from rich.style import Style
from rich.text import Text

from liblaf.grapes.typing import PathLike


def rich_location(
    name: str | None,
    function: str | None,
    line: int | None,
    file: PathLike | None = None,
    *,
    enable_link: bool = True,
    width: int | None = None,
) -> Text:
    if width:
        # TODO: truncate long name
        raise NotImplementedError
    file: Path | None = Path(file) if file is not None else None
    function = function or "<unknown>"
    line = line or 0
    if enable_link and file is not None and file.exists():
        return Text(
            f"{name}:{function}:{line}", style=Style(link=f"{file.as_uri()}#{line}")
        )
    return Text(f"{name}:{function}:{line}")
