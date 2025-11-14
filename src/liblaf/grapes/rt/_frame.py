import inspect
import types

from ._release_type import is_pre_release


def get_frame(depth: int = 1) -> types.FrameType | None:
    frame: types.FrameType | None = inspect.currentframe()
    while frame is not None and depth > 0:
        if not is_frame_hidden_from_logging(frame):
            depth -= 1
        frame = frame.f_back
    return frame


def is_frame_hidden_from_logging(frame: types.FrameType | None) -> bool:
    return frame is None or frame.f_globals.get("__tracebackhide__", False)


def is_frame_hidden_from_traceback(frame: types.FrameType | None) -> bool:
    if frame is None:
        return True
    if frame.f_locals.get("__tracebackhide__", False):
        return True
    name: str = frame.f_globals.get("__name__", "")
    return not is_pre_release(frame.f_code.co_filename, name)
