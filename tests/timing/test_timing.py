from collections.abc import Iterable

from liblaf.grapes.timing import BaseTimer, get_timer, timer


@timer()
def func() -> None: ...


def test_timer_with() -> None:
    with timer() as t:
        ...
    assert len(t) == 1


def test_timer_function() -> None:
    func()
    t: BaseTimer = get_timer(func)
    assert t.label == "func()"
    assert len(t) == 1


def test_timer_iterable() -> None:
    data: list[int] = list(range(10))
    wrapper: Iterable[int] = timer(data)
    result: list[int] = list(wrapper)
    t: BaseTimer = get_timer(wrapper)
    assert len(t) == len(data)
    assert result == data
    assert t.label == "Iterable"
