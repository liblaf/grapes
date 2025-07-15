from collections.abc import Sequence
from typing import override

import attrs
import loguru

from liblaf.grapes.logging import handler

from . import mixins
from ._abc import LoggingProfile


def default_handlers() -> Sequence["loguru.HandlerConfig"]:
    return [handler.rich_handler()]


def default_levels() -> Sequence["loguru.LevelConfig"]:
    return [{"name": "ICECREAM", "no": 15, "color": "<magenta><bold>", "icon": "🍦"}]


@attrs.define
class LoggingProfileDefault(
    mixins.LoggingProfileMixinLoguru,
    mixins.LoggingProfileMixinIcecream,
    mixins.LoggingProfileMixinExceptHook,
    mixins.LoggingProfileMixinUnraisableHook,
    LoggingProfile,
):
    handlers: Sequence["loguru.HandlerConfig"] | None = attrs.field(
        factory=default_handlers
    )
    levels: Sequence["loguru.LevelConfig"] | None = attrs.field(factory=default_levels)

    @override
    def init(self) -> None:
        self.configure_loguru()
        self.configure_icecream()
        self.configure_excepthook()
        self.configure_unraisablehook()
