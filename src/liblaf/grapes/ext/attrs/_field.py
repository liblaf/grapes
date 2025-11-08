from typing import Any

import attrs
import cytoolz as toolz

from liblaf.grapes.functools import wraps

from ._constants import METADATA_REPR


@wraps(attrs.field)
def field(*args, **kwargs) -> Any:
    if "repr" in kwargs:
        kwargs["metadata"] = toolz.assoc(
            kwargs.get("metadata", {}), METADATA_REPR, kwargs["repr"]
        )
    return attrs.field(*args, **kwargs)
