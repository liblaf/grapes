import functools
import sys
import types
import unittest.mock
from collections.abc import Callable, Iterable
from pathlib import Path

from loguru._get_frame import load_get_frame_function

from liblaf.grapes._config import config

_get_frame_original: Callable[[int], types.FrameType | None] = load_get_frame_function()


def _get_frame(depth: int = 0, /) -> types.FrameType | None:
    __tracebackhide__ = True
    frame: types.FrameType | None = _get_frame_original(0)
    while frame is not None:
        if not _should_hide(frame):
            if depth <= 0:
                return frame
            depth -= 1
        frame = frame.f_back
    msg = "call stack is not deep enough"
    raise ValueError(msg)


def _should_hide(frame: types.FrameType) -> bool:
    for name in ("__traceback_hide__", "__tracebackhide__"):
        if frame.f_locals.get(name, False):
            return True
    file: Path = Path(frame.f_code.co_filename)
    hide: bool = any(
        file.is_relative_to(path)
        for path in _get_hide_prefixes(tuple(config.logging.hide_frame.get()))
    )
    return hide


def _get_hide_prefixes(modules: Iterable[str] | None) -> list[Path]:
    if modules is None:
        modules = config.logging.hide_frame.get()
    return _get_hide_prefixes_cached(tuple(modules))


@functools.lru_cache
def _get_hide_prefixes_cached(modules: tuple[str]) -> list[Path]:
    paths: list[Path] = []
    for name in modules:
        module: types.ModuleType | None = sys.modules.get(name)
        if module is None:
            continue
        file: str | None = getattr(module, "__file__", None)
        if file is None:
            continue
        paths.append(Path(file).parent)
    return paths


def patch_loguru_get_frame(
    new: Callable[[int], types.FrameType | None] = _get_frame,
) -> None:
    # ! dirty hack
    patcher = unittest.mock.patch("loguru._logger.get_frame", new)
    patcher.start()
