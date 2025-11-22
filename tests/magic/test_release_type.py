import importlib.metadata

from packaging.version import Version

from liblaf.grapes import magic


def test_is_dev_release() -> None:
    version = Version(importlib.metadata.version("liblaf-grapes"))
    assert magic.is_dev_release(file=magic.__file__) == version.is_devrelease


def test_is_pre_release() -> None:
    version = Version(importlib.metadata.version("liblaf-grapes"))
    assert magic.is_dev_release(file=magic.__file__) == version.is_prerelease
