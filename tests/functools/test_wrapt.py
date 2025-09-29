from collections.abc import Callable
from typing import Any

import pytest

import liblaf.grapes.functools as ft


def decorator[C](func: C) -> C:
    @ft.decorator
    def wrapper(
        wrapped: Callable, _instance: Any, args: tuple, kwargs: dict[str, Any]
    ) -> Any:
        return wrapped(*args, **kwargs)

    proxy: C = wrapper(func)
    ft.wrapt_setattr(proxy, "exists", True)  # noqa: FBT003
    return proxy


class A:
    @decorator
    def method(self) -> None: ...


def test_wrapt_getattr() -> None:
    bound_cls = A.method
    ft.wrapt_setattr(bound_cls, "bound_exists", True)  # noqa: FBT003
    bound_instance = A().method
    ft.wrapt_setattr(bound_instance, "bound_exists", True)  # noqa: FBT003

    assert ft.wrapt_getattr(bound_cls, "exists")
    assert ft.wrapt_getattr(bound_instance, "exists")
    assert ft.wrapt_getattr(bound_cls, "bound_exists")
    assert ft.wrapt_getattr(bound_instance, "bound_exists")

    with pytest.raises(
        AttributeError, match="'function' object has no attribute '_self_missing'"
    ):
        ft.wrapt_getattr(bound_cls, "missing")
    with pytest.raises(
        AttributeError, match="'function' object has no attribute '_self_missing'"
    ):
        ft.wrapt_getattr(bound_instance, "missing")
    with pytest.raises(
        AttributeError, match="'function' object has no attribute '_self_bound_missing'"
    ):
        ft.wrapt_getattr(bound_cls, "bound_missing")
    with pytest.raises(
        AttributeError, match="'function' object has no attribute '_self_bound_missing'"
    ):
        ft.wrapt_getattr(bound_instance, "bound_missing")
