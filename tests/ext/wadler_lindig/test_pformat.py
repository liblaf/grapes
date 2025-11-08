import attrs
import numpy as np

from liblaf.grapes.ext.wadler_lindig import pformat


@attrs.define
class MyDataclass:
    x: list[str]
    y: np.ndarray


def test_pformat_attrs() -> None:
    obj = MyDataclass(["lorem", "ipsum", "dolor sit amet"], np.zeros((2, 3)))
    assert (
        pformat(obj, width=30, indent=4)
        == """\
MyDataclass(
    x=[
        'lorem',
        'ipsum',
        'dolor sit amet'
    ],
    y=f64[2,3](numpy)
)"""
    )
