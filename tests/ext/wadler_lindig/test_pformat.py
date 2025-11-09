import attrs
import numpy as np
import pydantic

from liblaf.grapes._config import config
from liblaf.grapes.ext.wadler_lindig import pformat


@attrs.define
class MyDataclassAttrs:
    x: list[str]
    y: np.ndarray


def test_pformat_attrs() -> None:
    obj = MyDataclassAttrs(x=["lorem", "ipsum", "dolor sit amet"], y=np.zeros((2, 3)))
    with config.pretty.short_arrays.overrides(True):  # noqa: FBT003
        assert (
            pformat(obj, width=30, indent=4)
            == """\
MyDataclassAttrs(
    x=[
        'lorem',
        'ipsum',
        'dolor sit amet'
    ],
    y=f64[2,3](numpy)
)"""
        )


class MyDataclassPydantic(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(arbitrary_types_allowed=True)
    x: list[str]
    y: np.ndarray


def test_pformat_pydantic() -> None:
    obj = MyDataclassPydantic(
        x=["lorem", "ipsum", "dolor sit amet"], y=np.zeros((2, 3))
    )
    with config.pretty.short_arrays.overrides(True):  # noqa: FBT003
        assert (
            pformat(obj, width=30, indent=4)
            == """\
MyDataclassPydantic(
    x=[
        'lorem',
        'ipsum',
        'dolor sit amet'
    ],
    y=f64[2,3](numpy)
)"""
        )
