import logging
import os
from collections.abc import Iterable
from pathlib import Path
from typing import IO, override

from liblaf.grapes.rich import get_console
from liblaf.grapes.rich.logging.handlers import RichHandler, RichHandlerColumn

type StrPath = str | os.PathLike[str]


class RichFileHandler(RichHandler):
    def __init__(
        self,
        filename: StrPath,
        mode: str = "w",
        *,
        encoding: str | None = None,
        errors: str | None = None,
        # RichHandler options
        columns: Iterable[RichHandlerColumn] | None = None,
        level: int = logging.NOTSET,
    ) -> None:
        filename = Path(filename)
        filename.parent.mkdir(parents=True, exist_ok=True)
        file: IO[str] = filename.open(mode=mode, encoding=encoding, errors=errors)
        console = get_console(file=file)
        super().__init__(console, columns=columns, level=level)

    @override
    def close(self) -> None:
        super().close()
        self.console.file.close()
