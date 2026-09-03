from collections.abc import Iterable, Mapping
from typing import Any, ClassVar

from rich.console import Console, ConsoleOptions, RenderResult
from rich.text import Text

from liblaf import conf


class Config(conf.BaseConfig):
    env_prefix: ClassVar[str] = "PPRINT_"

    hide_defaults: conf.Field[bool] = conf.field_bool(default=True)
    indent: conf.Field[Text] = field_text(default=INDENT)
    max_array: conf.Field[int] = conf.field_int(default=5)
    max_dict: conf.Field[int] = conf.field_int(default=4)
    max_level: conf.Field[int] = conf.field_int(default=6)
    max_list: conf.Field[int] = conf.field_int(default=6)
    max_long: conf.Field[int] = conf.field_int(default=40)
    max_other: conf.Field[int] = conf.field_int(default=30)
    max_string: conf.Field[int] = conf.field_int(default=30)


class Pretty:
    """One presentation with Rich, text, and display adapters."""

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult: ...

    def text(self, *, width: int = 88) -> str: ...

    # If console is None, use `rich.get_console()`.
    def show(self, *, console: Console | None = None) -> None: ...


def pretty(obj: Any, **kwargs) -> Pretty: ...


def format_frame_variables(
    frames: Iterable[Mapping[str, Any]], **kwargs
) -> tuple[tuple[str, ...], ...]: ...


# only the first shallowest appearance of repeated object is fully printed
# the other appearances are printed as <CustomClassA object at 0x7f8c9c0d1e50>
# or <CustomClassA object at x.field["key"][0].prop>
# when the path can fit inline, we should use path as reference, instead of memory address.
# when the path cannot fit inline, we should use memory address as reference.
# the fully printed appearance should be printed with a same reference as comment, so that the user can find the fully printed appearance easily.
# referable=False objects should not be deduplicated, and should be fully printed every time.
# by default, most objects are referable, except for some small objects like int, float, str, bool, None, Ellipsis, enum, etc scalars. which are not referable.


# Here are some use cases:


# `liblaf.pprint` should be able to pretty print dataclass-like objects using `fieldz`
# short arrays (each dim length < config.max_array) should be printed using default `__repr__`
# long arrays should use wadler-lindig like array summary (with framework, shape, device, dtype, etc.)


class CustomClassA:
    # if name is not given, use disambiguated class name
    # if begin is not given, use `(` with proper style
    # if end is not given, use `)` with proper style
    # or @pprint.list(name=..., begin=..., end=...) for list-like class
    # or @pprint.dict(name=..., begin=..., end=...) for dict-like class
    # the difference is size limit, and the default begin/end style
    # note that even if @pprint.list is used, the class can still have named fields, key-value pairs, etc.
    # by default, we should not use wadler-lindig group, but prettier's fill container.
    @pprint.container(name=..., begin=..., end=...)
    def __pretty__(self, ctx: pprint.Context):
        # `item` and `key_value`
        yield ctx.item(0, self)
        yield ctx.field("name", self.name)
        if not ctx.options.hide_defaults and self.x != X_DEFAULT:
            yield ctx.field("x", self.x)
        # or let pprint decide
        yield ctx.field("y", self.y, Y_DEFAULT)
        yield ctx.key_value("key", self.key)


# User can also register custom pretty printer for third party classes:


@pprint.register(ThirdPartyClass)
# or lazily register with `@pprint.register("module.ThirdPartyClass")`
@pprint.container(name=..., begin=..., end=..., referable=True)
def _pprint_third_party_class(obj: ThirdPartyClass, ctx: pprint.Context): ...


# or more direct control without `@pprint.container` decorator:


@pprint.register(ThirdPartyClass)
def _pprint_third_party_class(obj: ThirdPartyClass, ctx: pprint.Context):
    # You can determine what API to expose here for easy customization.
    return ctx.leaf(custom_text, referable=False)


# The library will also be used by `liblaf.traceback` to pretty print traceback with repeated objects. `format_frame_variables` is the narrow integration seam for stack variables.
# We should include frame info in object path to track them.
# Here shallowest appearance does not mean the first appearance in the stack trace, but the first appearance in the object graph. So we can think of stack as a flat list of frames, and each frame is a flat list of variables. The shallowest appearance is the first appearance in the object graph, which may be in a different frame than the shallowest frame.
# This library should only handle variables, not the formatting of source code, line numbers, etc. The `liblaf.traceback` library should handle that.
# A Frame should be something like:
# a = ...
# some_long_variable = ...
# b = CustomClassA(
# |   ...
# )
# note that we don't have to align `=` like rich does.
