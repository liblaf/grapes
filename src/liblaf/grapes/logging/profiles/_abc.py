import abc

import attrs


@attrs.define
class LoggingProfile(abc.ABC):
    @abc.abstractmethod
    def init(self) -> None: ...
