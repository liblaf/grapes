# ref: <https://toolz.readthedocs.io/en/latest/tips-and-tricks.html>

import itertools
from collections.abc import Container, Iterable, Iterator, Mapping
from typing import Any

import tlz


def pick[KT, VT](allowlist: Container[KT], dictionary: Mapping[KT, VT]) -> dict[KT, VT]:
    """Return a subset of the provided dictionary with keys contained in the allowlist.

    Examples:
        >>> alphabet = {"a": 1, "b": 2, "c": 3, "d": 4}
        >>> pick(["a", "b"], alphabet)
        {'a': 1, 'b': 2}
    """
    return tlz.keyfilter(lambda k: k in allowlist, dictionary)


def omit[KT, VT](denylist: Container[KT], dictionary: Mapping[KT, VT]) -> dict[KT, VT]:
    """Return a subset of the provided dictionary with keys not contained in the denylist.

    Examples:
        >>> alphabet = {"a": 1, "b": 2, "c": 3, "d": 4}
        >>> omit(["a", "b"], alphabet)
        {'c': 3, 'd': 4}
    """
    return tlz.keyfilter(lambda k: k not in denylist, dictionary)


def compact[T](iterable: Iterable[T | None]) -> Iterator[T]:
    """Filter an iterable on "truthy" values.

    Examples:
        >>> results = [0, 1, 2, None, 3, False]
        >>> list(compact(results))
        [1, 2, 3]
    """
    return tlz.filter(None, iterable)


def keyjoin[KT, VT](
    leftkey: KT,
    leftseq: Iterable[Mapping[KT, VT]],
    rightkey: KT,
    rightseq: Iterable[Mapping[KT, VT]],
) -> Iterator[Mapping[KT, VT]]:
    """Inner join two sequences of dictionaries on specified keys, merging matches with right value precedence.

    Examples:
        >>> people = [
        ...     {"id": 0, "name": "Anonymous Guy", "location": "Unknown"},
        ...     {"id": 1, "name": "Karan", "location": "San Francisco"},
        ...     {"id": 2, "name": "Matthew", "location": "Oakland"},
        ... ]
        >>> hobbies = [
        ...     {"person_id": 1, "hobby": "Tennis"},
        ...     {"person_id": 1, "hobby": "Acting"},
        ...     {"person_id": 2, "hobby": "Biking"},
        ... ]
        >>> list(keyjoin("id", people, "person_id", hobbies))
        [{'id': 1, 'name': 'Karan', 'location': 'San Francisco', 'person_id': 1, 'hobby': 'Tennis'}, {'id': 1, 'name': 'Karan', 'location': 'San Francisco', 'person_id': 1, 'hobby': 'Acting'}, {'id': 2, 'name': 'Matthew', 'location': 'Oakland', 'person_id': 2, 'hobby': 'Biking'}]
    """
    return itertools.starmap(tlz.merge, tlz.join(leftkey, leftseq, rightkey, rightseq))


def areidentical(*seqs: Iterable[Any]) -> bool:
    """Determine if sequences are identical element-wise. This lazily evaluates the sequences and stops as soon as the result is determined.

    Examples:
        >>> areidentical([1, 2, 3], (1, 2, 3))
        True

        >>> areidentical([1, 2, 3], [1, 2])
        False
    """
    return not any(tlz.diff(*seqs, default=object()))
