from typing import Generator

import pytest

from src.database import engine
from src.db_tables import tables

pytest_plugins = ["docker_compose"]


@pytest.fixture(scope="function", autouse=True)
def reset_tables() -> Generator[None, None, None]:
    [table.__table__.create(engine) for table in tables]
    yield
    [table.__table__.drop(engine) for table in tables]
