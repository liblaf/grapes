# formerly `liblaf.pineapple`.

# This project is used to cache expensive function calls to disk.
# Different from alternatives, we want each folder to be a cache entry
# contents saved on disk should be standard format (e.g. json, numpy, vtk, etc.) instead of pickle, so that user can easily inspect the cache entry.
# when multiple processes are trying to compute the same key, only one process should compute it, and other processes should wait for the result. We can use file lock to achieve this.
# In other words, no recomputation should be done for the same key, even if multiple processes are trying to compute it at the same time.

# The library should support both sync and async functions
# We should provider decorators and dict-like API for direct interaction with disk cache. The dict-like API should also support both sync and async usage.

# To avoid too much disk usage, we should provide a default-enabled purge mechanism to remove old unused cache entries. Default size limit to 4GiB.

from pathlib import Path
from typing import Any


def inputs_writer(folder: Path, *args, **kwargs) -> None:
    # Write the inputs to the folder
    # By defaults, use pretty print and write to folder / `inputs.txt`.
    # If `liblaf.pprint` is available, we should use that.
    ...


def output_writer(folder: Path, output: Any) -> None:
    # Write the output to the folder
    # By defaults, we should try several standard formats:
    # - if json-serializable, write to folder / `output.json`
    # - if numpy array, write to folder / `output.npy`
    # - if dict of numpy arrays, write to folder / `output.npz` (compressed)
    # - if pyvista object, write to folder / `output.vtu/.vtp/.vtm/.vti` depending on the type
    # - if torch tensor, write to folder / `output.pt`
    # - if pandas / polars dataframe, write to folder / `output.parquet`
    # - if not serializable, use joblib dump `output.joblib.gz`. If we are not mistaken, joblib is better pickle.
    # All those dependencies should be optional.
    # joblib is a dependency because we need it as last resort.
    ...


def output_reader(folder: Path) -> Any:
    # Read the output from the folder
    # By defaults, we should use the same logic as output_writer to determine the format and read it back.
    ...


@cache.cache(
    inputs_writer=...,
    output_writer=...,
    output_reader=...,
    purge=Purge(size="4G"),
    key=lambda *args, **kwargs: ...,  # by default, use `joblib.hash`
)
def some_expensive_function(*args, **kwargs) -> Any: ...


async def inputs_writer(folder: Path, *args, **kwargs) -> None:
    # Write the inputs to the folder
    ...


async def output_writer(folder: Path, output: Any) -> None:
    # Write the output to the folder
    ...


async def output_reader(folder: Path) -> Any:
    # Read the output from the folder
    ...


@cache.cache(inputs_writer=..., output_writer=..., output_reader=...)
async def some_expensive_function(*args, **kwargs) -> Any: ...
