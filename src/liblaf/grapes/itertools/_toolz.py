# ref: <https://toolz.readthedocs.io/en/latest/tips-and-tricks.html>

import itertools
from collections.abc import Container, Iterable, Iterator, Mapping
from typing import Any

import tlz


def pick[KT, VT](allowlist: Container[KT], dictionary: Mapping[KT, VT]) -> dict[KT, VT]:
    return tlz.keyfilter(lambda k: k in allowlist, dictionary)


def omit[KT, VT](denylist: Container[KT], dictionary: Mapping[KT, VT]) -> dict[KT, VT]:
    return tlz.keyfilter(lambda k: k not in denylist, dictionary)


def compact[T](iterable: Iterable[T | None]) -> Iterator[T]:
    return tlz.filter(None, iterable)


def keyjoin[KT, VT](
    leftkey: KT,
    leftseq: Iterable[Mapping[KT, VT]],
    rightkey: KT,
    rightseq: Iterable[Mapping[KT, VT]],
) -> Iterator[Mapping[KT, VT]]:
    return itertools.starmap(tlz.merge, tlz.join(leftkey, leftseq, rightkey, rightseq))


def areidentical(*seqs: Iterable[Any]) -> bool:
    return not any(tlz.diff(*seqs, default=object()))
