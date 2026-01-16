import pytest
import rich
from environs import env

from liblaf.grapes import conf


def test_field_misc() -> None:
    a: conf.Field[int] = conf.Field(name="a", default=42, getter=env.int)
    assert a.name == "a"
    assert repr(a) == "Field(name='a', value=42)"
    assert repr(a)
    rich.print(a)


def test_field_default() -> None:
    a: conf.Field[int] = conf.Field(name="a", default=42, getter=env.int)
    assert a.get() == 42


def test_field_factory() -> None:
    a: conf.Field[int] = conf.Field(name="a", factory=lambda: 42, getter=env.int)
    assert a.get() == 42


def test_field_env(monkeypatch: pytest.MonkeyPatch) -> None:
    with monkeypatch.context() as m:
        m.setenv("TEST_A", "100")
        a: conf.Field[int] = conf.Field(name="a", env="TEST_A", getter=env.int)
        assert a.get() == 100


def test_field_overrides() -> None:
    a: conf.Field[int] = conf.Field(name="a", getter=env.int)
    a.set(1)
    with a.overrides(2):
        assert a.get() == 2
    assert a.get() == 1
