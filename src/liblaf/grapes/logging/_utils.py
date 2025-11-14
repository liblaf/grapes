import functools
import importlib.machinery
import importlib.util
import types
from pathlib import Path


def should_hide(frame: types.FrameType) -> bool:
    """.

    Reference:
        1. [Lib/logging/__init__.py#L173-L199 · python/cpython](https://github.com/python/cpython/blob/781cc68c3c814e46e6a74c3a6a32e0f9f8f7eb11/Lib/logging/__init__.py#L173-L199)
    """
    filename: str = frame.f_code.co_filename
    if "importlib" in filename or "_bootstrap" in filename:
        return True
    path: Path = Path(filename).resolve()
    for prefix in _prefixes():
        if path.is_relative_to(prefix):
            return True
    return frame.f_locals.get("__tracebackhide__", False)


@functools.cache
def _prefixes() -> list[Path]:
    paths: list[Path] = []
    for name in ("logging", "lazy_loader"):
        spec: importlib.machinery.ModuleSpec | None = importlib.util.find_spec(name)
        if spec is None or spec.submodule_search_locations is None:
            continue
        paths.extend(
            Path(location).resolve() for location in spec.submodule_search_locations
        )
    return paths
