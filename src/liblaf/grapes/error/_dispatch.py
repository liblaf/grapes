from collections.abc import Callable, Mapping, Sequence
from typing import Self

import attrs

from liblaf.grapes import pretty


@attrs.define
class Params:
    args: Sequence = ()
    kwargs: Mapping = {}


@attrs.define
class DispatchLookupError(LookupError):
    func: Callable
    params: Params

    @classmethod
    def new(cls, func: Callable, args: Sequence, kwargs: Mapping) -> Self:
        return cls(func=func, params=Params(args=args, kwargs=kwargs))

    def __str__(self) -> str:
        pretty_call: str = pretty.pretty_call(
            self.func, self.params.args, self.params.kwargs
        )
        return f"`{pretty_call}` could not be resolved."
