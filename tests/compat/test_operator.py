import pytest

from liblaf.grapes import compat


@pytest.fixture(scope="package")
def data() -> dict[str, int]:
    return {"a": 1, "b": 2}


def test_contains(data: dict[str, int]) -> None:
    assert compat.contains(data, "a")


def test_contains_deprecated(data: dict[str, int]) -> None:
    with pytest.deprecated_call():
        assert compat.contains(data, "c", deprecated_keys=["missing", "b"])


def test_contains_missing(data: dict[str, int]) -> None:
    assert not compat.contains(data, "missing")


def test_getitem(data: dict[str, int]) -> None:
    assert compat.getitem(data, "a") == data["a"]


def test_getitem_deprecated(data: dict[str, int]) -> None:
    with pytest.deprecated_call():
        assert compat.getitem(data, "c", deprecated_keys=["missing", "b"]) == data["b"]


def test_getitem_missing(data: dict[str, int]) -> None:
    with pytest.raises(KeyError):
        compat.getitem(data, "missing")
