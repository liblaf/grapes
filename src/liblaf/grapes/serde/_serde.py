import os
import warnings
from pathlib import Path
from typing import Any, override

import autoregistry

from liblaf import grapes

from . import AbstractSerializer, json, toml, yaml

SERIALIZERS = autoregistry.Registry()
SERIALIZERS["json"] = json
SERIALIZERS["toml"] = toml
SERIALIZERS["yaml"] = yaml
SERIALIZERS["yml"] = yaml


class AutoSerializer(AbstractSerializer):
    @override
    def load(
        self, fpath: str | os.PathLike[str], *, ext: str | None = None, **kwargs
    ) -> Any:
        serializer: AbstractSerializer = self.get_serializer(fpath, ext=ext)
        return serializer.load(fpath, **kwargs)

    @override
    def loads(self, data: str, *, ext: str | None = None, **kwargs) -> Any:
        serializer: AbstractSerializer = self.get_serializer(fpath="", ext=ext)
        return serializer.loads(data, **kwargs)

    @override
    def dump(
        self,
        fpath: str | os.PathLike[str],
        data: Any,
        *,
        ext: str | None = None,
        **kwargs,
    ) -> None:
        serializer: AbstractSerializer = self.get_serializer(fpath, ext=ext)
        serializer.dump(fpath, data, **kwargs)

    @override
    def dumps(self, data: Any, *, ext: str | None = None, **kwargs) -> str:
        serializer: AbstractSerializer = self.get_serializer(fpath="", ext=ext)
        return serializer.dumps(data, **kwargs)

    def get_serializer(
        self, fpath: str | os.PathLike[str], *, ext: str | None = None
    ) -> AbstractSerializer:
        if ext is None:
            fpath: Path = grapes.as_path(fpath)
            ext = fpath.suffix.lstrip(".")
        return SERIALIZERS[ext]  # pyright: ignore[reportReturnType]


auto = AutoSerializer()
load = auto.load
loads = auto.loads
dump = auto.dump
dumps = auto.dumps


@warnings.deprecated("Use `dump()` instead of `serialize()`")
def serialize(
    fpath: str | os.PathLike[str], data: Any, *, ext: str | None = None
) -> None:
    return dump(fpath, data, ext=ext)


@warnings.deprecated("Use `load()` instead of `deserialize()`")
def deserialize(fpath: str | os.PathLike[str], *, ext: str | None = None) -> Any:
    return load(fpath, ext=ext)
