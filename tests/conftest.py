import pytest
from app.person import Person


@pytest.fixture
def todo_1():
    return {"userId": 1, "id": 1, "title": "delectus aut autem", "completed": False}


@pytest.fixture
def person_1():
    p1 = Person("John", 36)
    return p1
