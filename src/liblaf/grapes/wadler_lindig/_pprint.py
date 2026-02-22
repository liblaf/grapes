from typing import Any, Unpack

import wadler_lindig as wl

from ._options import WadlerLindigOptions, make_kwargs


def pprint(obj: Any, **kwargs: Unpack[WadlerLindigOptions]) -> None:
    """Pretty-prints an object to stdout.

    Examples:
        array:

        >>> import numpy as np
        >>> pprint(np.zeros((2, 3)))
        array([[0., 0., 0.],
               [0., 0., 0.]])
        >>> pprint(np.zeros((20, 30)))
        f64[20,30](numpy)

        datetime:

        >>> import datetime
        >>> pprint(datetime.datetime(1970, 1, 1, tzinfo=datetime.UTC))
        1970-01-01T00:00:00+00:00

        dataclass:

        >>> import dataclasses
        >>> import numpy as np
        >>> @dataclasses.dataclass
        ... class MyDataclass:
        ...     x: list[str]
        ...     y: np.ndarray
        >>> obj = MyDataclass(["lorem", "ipsum", "dolor sit amet"], np.zeros((2, 3)))
        >>> pprint(obj, width=30, indent=4)
        MyDataclass(
            x=[
                'lorem',
                'ipsum',
                'dolor sit amet'
            ],
            y=array([[0., 0., 0.],
                     [0., 0., 0.]])
        )

        dict:

        >>> pprint({"jack": 4098, "sjoerd": 4127})
        {'jack': 4098, 'sjoerd': 4127}

        pydantic:

        >>> import pydantic
        >>> class MyModel(pydantic.RootModel[list[str]]): ...
        >>> obj = MyModel(["lorem", "ipsum", "dolor sit amet"])
        >>> pprint(obj)
        MyModel['lorem', 'ipsum', 'dolor sit amet']

        rich.repr:

        >>> import rich
        >>> class Bird:
        ...     def __rich_repr__(self):
        ...         yield "penguin"
        ...         yield "eats", ["fish"]
        ...         yield "fly", False, True
        ...         yield "extinct", False, False
        >>> pprint(Bird())
        Bird('penguin', eats=['fish'], fly=False)
    """
    kwargs: WadlerLindigOptions = make_kwargs(**kwargs)
    return wl.pprint(obj, **kwargs)
