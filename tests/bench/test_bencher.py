import random
from collections.abc import Generator, Mapping, Sequence

from liblaf.grapes.bench import Bencher, BenchResults


def test_bencher() -> None:
    bencher = Bencher()

    @bencher.setup
    def setup() -> Generator[tuple[Sequence, Mapping]]:
        for n in [1, 2, 4, 8]:
            data: list[int] = list(range(n))
            random.shuffle(data)
            yield (data,), {}

    @bencher.bench(label="stdlib")
    def stdlib_sort(arr: list[int]) -> list[int]:
        return sorted(arr)

    @bencher.bench(label="bubble")
    def bubble_sort(arr: list[int]) -> list[int]:
        arr = arr.copy()
        n: int = len(arr)
        for i in range(n):
            swapped: bool = False
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr

    results: BenchResults = bencher.run()
    assert all(len(timings) == 4 for timings in results.timings.values())
    assert len(results.sizes) == 4
    assert results.outputs["stdlib"] == results.outputs["bubble"]
    assert results.timings.keys() == {"stdlib", "bubble"}
