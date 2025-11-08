import attrs
import wadler_lindig as wl

from liblaf.grapes.ext.attrs import define
from liblaf.grapes.ext.wadler_lindig import pformat


@define
class SomeClass:
    a_number: int = 42
    list_of_numbers: list[int] = attrs.Factory(list)


def test_define() -> None:
    obj = SomeClass()
    assert wl.pformat(obj) == pformat(obj)
