from pathlib import Path

from liblaf.grapes.conf import BaseConfig, Field, field


class ConfigLogging(BaseConfig):
    datefmt: Field[str] = field(default="YYYY-MM-DD HH:mm:ss.SSS", env="LOG_DATEFMT")
    file: Field[Path | None] = field(default=None, env="LOG_FILE")
    hide_frame: Field[list[str]] = field(factory=lambda: ["rich.progress"])
    level: Field[int | str] = field(default="TRACE")
    time_relative: Field[bool] = field(default=True, env="LOG_TIME_RELATIVE")
