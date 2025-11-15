import pytest

from liblaf.grapes.icecream import ICECREAM, install


def test_icecream(caplog: pytest.LogCaptureFixture) -> None:
    install()
    a: int = 1
    with caplog.at_level(ICECREAM, __name__):
        assert ic() is None
        assert ic(a) == a
        assert ic(a, a) == (a, a)
        assert ic(1) == 1
        assert ic(1, 1) == (1, 1)
    for record in caplog.records:
        assert record.name == __name__
        assert record.levelno == ICECREAM
    assert caplog.records[0].message.startswith("🍦")
    assert caplog.records[1].message == "a: 1"
    assert caplog.records[2].message == "a: 1, a: 1"
    assert caplog.records[3].message == "1"
    assert caplog.records[4].message == "1, 1"
