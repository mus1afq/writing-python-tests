from app.person import Person


def test_person_obj_str(person_1):
    """Test object string."""
    assert str(person_1) == "John(36)"


def test_person_created(person_1):
    """Test instance."""
    assert isinstance(person_1, Person)


def test_person_intro(person_1):
    """Test object methods."""
    assert person_1.greeting() == "Hello my name is John"
