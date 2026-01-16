from collections.abc import Iterable

from liblaf.grapes.rich.progress import track


def test_rich_progress() -> None:
    wrapped: list[int] = list(range(10))
    wrapper: Iterable[int] = track(wrapped)
    result: list[int] = list(wrapper)
    assert result == wrapped
