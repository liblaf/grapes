from typing import Any, Unpack

import wadler_lindig as wl
from rich.repr import RichReprResult

from liblaf.grapes.wadler_lindig._typing import WadlerLindigOptions

from ._type import pdoc_type


def pdoc_rich_repr(
    obj: Any, **kwargs: Unpack[WadlerLindigOptions]
) -> wl.AbstractDoc | None:
    if not hasattr(obj, "__rich_repr__"):
        return None
    repr_result: RichReprResult | None = obj.__rich_repr__()
    if repr_result is None:
        return None
    cls: type = type(obj)
    args: list[Any] = []
    pairs: list[tuple[str, Any]] = []
    for field in repr_result:
        name: str
        value: Any
        default: Any
        if isinstance(field, tuple):
            if len(field) == 2:
                name, value = field
                pairs.append((name, value))
            elif len(field) == 3:
                name, value, default = field
                if kwargs.get("hide_defaults", True) and value is default:
                    continue
                pairs.append((name, value))
        else:
            value = field
            args.append(value)
    return wl.bracketed(
        begin=pdoc_type(cls, dataclass=True, **kwargs) + wl.TextDoc("("),
        docs=[wl.pdoc(arg, **kwargs) for arg in args] + wl.named_objs(pairs, **kwargs),
        sep=wl.comma,
        end=wl.TextDoc(")"),
        indent=kwargs.get("indent", 2),
    )
