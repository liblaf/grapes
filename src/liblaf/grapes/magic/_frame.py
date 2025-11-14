import inspect
import types
from collections.abc import Callable

from ._release_type import is_pre_release


def hidden_from_logging(frame: types.FrameType | None) -> bool:
    return frame is None or frame.f_globals.get("__tracebackhide__", False)


def hidden_from_traceback(frame: types.FrameType | None) -> bool:
    if frame is None:
        return True
    if frame.f_locals.get("__tracebackhide__", False):
        return True
    name: str = frame.f_globals.get("__name__", "")
    return not is_pre_release(frame.f_code.co_filename, name)


def get_frame(
    depth: int = 1,
    hidden: Callable[[types.FrameType], bool] | None = hidden_from_traceback,
) -> types.FrameType | None:
    frame: types.FrameType | None = inspect.currentframe()
    while frame is not None and depth > 0:
        if hidden is None or not hidden(frame):
            depth -= 1
        frame = frame.f_back
    return frame
