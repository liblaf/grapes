from collections.abc import Sequence

import attrs
import loguru
import loguru._logger
from loguru import logger


@attrs.define(slots=False)
class LoggingProfileMixinLoguru:
    handlers: Sequence["loguru.HandlerConfig"] | None = attrs.field(default=None)
    levels: Sequence["loguru.LevelConfig"] | None = attrs.field(default=None)

    def configure_loguru(
        self,
        handlers: Sequence["loguru.HandlerConfig"] | None = None,
        levels: Sequence["loguru.LevelConfig"] | None = None,
    ) -> None:
        if handlers is None:
            handlers = self.handlers or []
        if levels is None:
            levels = self.levels or []

        self.handlers = handlers
        self.levels = levels

        for level in levels:
            self.level(**level)
        logger.configure(handlers=handlers)

    def level(
        self,
        name: str,
        no: int | None = None,
        color: str | None = None,
        icon: str | None = None,
    ) -> "loguru.Level":
        if name in self._core.levels and no == logger.level(name).no:
            no = None  # skip update severity no
        return logger.level(name=name, no=no, color=color, icon=icon)

    @property
    def _core(self) -> loguru._logger.Core:
        return logger._core  # pyright: ignore[reportAttributeAccessIssue] # noqa: SLF001
