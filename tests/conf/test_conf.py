import pytest

from liblaf.grapes import conf


class Config(conf.BaseConfig):
    a: conf.Field[int] = conf.int(default=0)


@pytest.fixture(scope="package")
def config() -> Config:
    return Config()


def test_overrides(config: Config) -> None:
    with config.a.overrides(1):
        assert config.a.get() == 1
