from app.main import full_name


def test_full_name():
    person_1 = full_name("John", "Doe")
    assert person_1 == "John Doe"
