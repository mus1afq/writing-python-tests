from app.person import Person

#running tests on stringß
def test_person_obj_str(person_1):
    assert str(person_1) == "John(36)"


def test_person_created(person_1):
    assert isinstance(person_1, Person)
