import pytest

from liblaf.grapes.icecream import ic


def test_icecream(caplog: pytest.LogCaptureFixture) -> None:
    a: int = 1
    with caplog.at_level(15, __name__):
        assert ic() is None
        assert ic(a) == a
        assert ic(a, a) == (a, a)
    assert len(caplog.records) == 3
    assert caplog.records[0].message.startswith("🍦")
    assert caplog.records[1].message == "a: 1"
    assert caplog.records[2].message == "a: 1, a: 1"
