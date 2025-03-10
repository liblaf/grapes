from pathlib import Path
from typing import Any

import pytest

from liblaf import grapes


@pytest.mark.parametrize("suffix", [".json", ".toml", ".yaml", ".yml"])
def test_json(data: Any, suffix: str, tmp_path: Path) -> None:
    file: Path = tmp_path / f"data{suffix}"
    grapes.dump(file, data)
    assert grapes.load(file) == data
