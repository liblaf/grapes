import logging
from collections.abc import Hashable, Mapping

import attrs
import cachetools

from ._by_name import FilterByName
from ._by_version import FilterByVersion
from ._once import FilterOnce
from ._utils import as_levelno


@attrs.define
class CompositeFilter:
    by_name: FilterByName = attrs.field(factory=lambda: FilterByName())
    by_version: FilterByVersion = attrs.field(factory=lambda: FilterByVersion())
    level: int = attrs.field(default=logging.INFO)
    once: FilterOnce = attrs.field(factory=FilterOnce)

    _cache: cachetools.LRUCache[Hashable, int] = attrs.field(
        repr=False, init=False, factory=lambda: cachetools.LRUCache(maxsize=1024)
    )

    def __init__(self, by_name: Mapping[str, int | str] | None = None) -> None:
        if by_name is None:
            by_name = {"__main__": logging.NOTSET}
        level: int = as_levelno(by_name.get("", logging.INFO))
        self.__attrs_init__(by_name=FilterByName(by_name), level=level)  # pyright: ignore[reportAttributeAccessIssue]

    def filter(self, record: logging.LogRecord) -> bool:
        if not self.once(record):
            return False
        level: int = self.get_level(record)
        return record.levelno >= level

    def get_level(self, record: logging.LogRecord) -> int:
        level: int = self._cache.get(record.name, -1)
        if level == -1:
            level = self._get_level_uncached(record) or self.level
            self._cache[record.name] = level
        return level

    def _get_level_uncached(self, record: logging.LogRecord) -> int | None:
        level: int | None = self.by_name.get_level(record)
        if level is not None:
            return level
        level = self.by_version.get_level(record)
        if level is not None:
            return level
        return None
