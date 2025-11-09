from pathlib import Path

from liblaf.grapes.conf import BaseConfig, Field, field


class ConfigLogging(BaseConfig):
    file: Field[Path | None] = field(default=None)
    level: Field[int | str] = field(default="TRACE")
