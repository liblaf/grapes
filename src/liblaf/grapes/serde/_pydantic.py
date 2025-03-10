import os
import warnings
from typing import Any

import pydantic

from liblaf import grapes

from . import dump, load


def load_pydantic[C: pydantic.BaseModel](
    fpath: str | os.PathLike[str], cls: type[C], *, ext: str | None = None, **kwargs
) -> C:
    data: Any = load(fpath, ext=ext, **kwargs)
    return cls.model_validate(data)


def dump_pydantic(
    fpath: str | os.PathLike[str],
    data: pydantic.BaseModel,
    *,
    ext: str | None = None,
    # pydantic.BaseModel.model_dump(**kwargs)
    context: Any | None = None,
    by_alias: bool = False,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False,
    round_trip: bool = False,
    serialize_as_any: bool = False,
) -> None:
    dump(
        fpath,
        data.model_dump(
            context=context,
            by_alias=by_alias,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
            round_trip=round_trip,
            serialize_as_any=serialize_as_any,
        ),
        ext=ext,
    )


@warnings.deprecated("Use `dump_pydantic()` instead of `save_pydantic()`")
def save_pydantic(
    fpath: str | os.PathLike[str],
    data: pydantic.BaseModel,
    *,
    ext: str | None = None,
    # pydantic.BaseModel.model_dump(**kwargs)
    context: Any | None = None,
    by_alias: bool = False,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False,
    round_trip: bool = False,
    serialize_as_any: bool = False,
) -> None:
    """Save a Pydantic model to a file using the specified serialization options.

    Args:
        fpath: The file path where the data should be saved.
        data: The Pydantic model instance to be serialized and saved.
        ext: The file extension to use.
        context: Additional context for the serialization.
        by_alias: Whether to use the alias names defined in the model.
        exclude_unset: Whether to exclude unset fields from the serialized output.
        exclude_defaults: Whether to exclude fields with default values from the serialized output.
        exclude_none: Whether to exclude fields with None values from the serialized output.
        round_trip: Whether to enable round-trip serialization.
        serialize_as_any: Whether to serialize the model as any type.
    """
    grapes.serialize(
        fpath,
        data.model_dump(
            context=context,
            by_alias=by_alias,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
            round_trip=round_trip,
            serialize_as_any=serialize_as_any,
        ),
        ext=ext,
    )
