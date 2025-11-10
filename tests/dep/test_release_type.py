import importlib.metadata

from packaging.version import Version

from liblaf.grapes import rt


def test_is_dev_release() -> None:
    version = Version(importlib.metadata.version("liblaf-grapes"))
    assert rt.is_dev_release(file=rt.__file__) == version.is_devrelease


def test_is_pre_release() -> None:
    version = Version(importlib.metadata.version("liblaf-grapes"))
    assert rt.is_dev_release(file=rt.__file__) == version.is_prerelease
