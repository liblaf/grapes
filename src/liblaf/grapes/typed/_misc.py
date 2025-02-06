import os
import types

type ClassInfo = type | types.UnionType | tuple[ClassInfo, ...]
type StrPath = str | os.PathLike[str]
