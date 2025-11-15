import builtins

from ._icecream import ic


def install() -> None:
    builtins.ic = ic  # pyright: ignore[reportAttributeAccessIssue]
