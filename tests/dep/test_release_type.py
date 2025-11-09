from liblaf.grapes import rt


def test_is_dev_release() -> None:
    assert rt.is_dev_release(file=rt.__file__)


def test_is_pre_release() -> None:
    assert rt.is_pre_release(file=rt.__file__)
