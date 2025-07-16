from collections.abc import Callable
from typing import Any

import pytest

from liblaf.grapes import functools as _ft


def decorator[C](func: C) -> C:
    @_ft.decorator
    def wrapper(
        wrapped: Callable, _instance: Any, args: tuple, kwargs: dict[str, Any]
    ) -> Any:
        return wrapped(*args, **kwargs)

    proxy: C = wrapper(func)
    proxy._self_exists = True  # pyright: ignore[reportAttributeAccessIssue] # noqa: SLF001
    return proxy


class A:
    @decorator
    def method(self) -> None: ...


def test_unbind_getattr() -> None:
    bound_cls = A.method
    bound_cls._self_bound_exists = True  # pyright: ignore[reportFunctionMemberAccess] # noqa: SLF001
    bound_instance = A().method
    bound_instance._self_bound_exists = True  # pyright: ignore[reportAttributeAccessIssue] # noqa: SLF001

    assert _ft.unbind_getattr(bound_cls, "_self_exists")
    assert _ft.unbind_getattr(bound_instance, "_self_exists")
    assert _ft.unbind_getattr(bound_cls, "_self_bound_exists")
    assert _ft.unbind_getattr(bound_instance, "_self_bound_exists")

    with pytest.raises(
        AttributeError, match="'function' object has no attribute '_self_missing'"
    ):
        _ft.unbind_getattr(bound_cls, "_self_missing")
    with pytest.raises(
        AttributeError, match="'function' object has no attribute '_self_missing'"
    ):
        _ft.unbind_getattr(bound_instance, "_self_missing")
    with pytest.raises(
        AttributeError, match="'function' object has no attribute '_self_bound_missing'"
    ):
        _ft.unbind_getattr(bound_cls, "_self_bound_missing")
    with pytest.raises(
        AttributeError, match="'function' object has no attribute '_self_bound_missing'"
    ):
        _ft.unbind_getattr(bound_instance, "_self_bound_missing")
