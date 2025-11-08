from liblaf.grapes import dep


def test_is_dev_release() -> None:
    assert dep.is_dev_release(file=dep.__file__)


def test_is_pre_release() -> None:
    assert dep.is_pre_release(file=dep.__file__)
