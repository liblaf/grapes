# This library should cover standard traceback workflows with more customization
# and Rich output. Familiar names are useful where they describe the result, but
# compatibility with the standard library API is not a goal.


from rich.console import Console


class Config(conf.BaseConfig):
    limit: conf.Field[int] = conf.field_int(default=100)
    hide_stable_release: conf.Field[bool] = conf.field_bool(default=True)
    capture_locals: conf.Field[bool] = conf.field_bool(default=True)
    locals_hide_sunder: conf.Field[bool] = conf.field_bool(default=True)
    locals_hide_dunder: conf.Field[bool] = conf.field_bool(default=True)
    suppress: conf.Field[list[str]] = conf.field_list(
        default=[]
    )  # can be path prefix or module prefix


class ExceptionRenderer:
    """Width-aware Rich presentation of one exception."""


def render_exception(exc: BaseException, /, **options) -> ExceptionRenderer: ...
def format_exception(exc: BaseException, /, **options) -> str: ...
def print_exception(
    exc: BaseException, /, *, console: Console | None = None, **options
) -> None: ...


# frames with `__tracebackhide__ = True` should be dimmed and abbreviated in one line.
# frames from release with stable version (is stable release) should be dimmed and abbreviated in one line.
# We should show the full statement of the frame line source code, instead of simple lines around.
# Don't refresh linecache because even if we change source code on disk, running code won't be affected, and we should show the source code of the running code, not the source code on disk.


# This library will be used by `liblaf.logging` to pretty print log messages with stack traces.
# To avoid hard dependency on `liblaf.pprint`, we should allow custom variable printting. We should use `liblaf.pprint` when it's available, otherwise use standard `pprint`.
