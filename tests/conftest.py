import pytest


@pytest.fixture
def todo_1():
    return {"userId": 1, "id": 1, "title": "delectus aut autem", "completed": False}
