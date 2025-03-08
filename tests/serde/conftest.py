from typing import Any

import pytest


@pytest.fixture(scope="package")
def data() -> Any:
    return {"x": 1, "y": 2}
