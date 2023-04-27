from app.apicalls import get_todo_item


def test_get_todo_item_success():
    """Test response status is 200."""
    response = get_todo_item(1)
    assert response.status_code == 200


def test_todo_item_data(todo_1):
    """Test correct data in response."""
    response = get_todo_item(1)
    assert response.json() == todo_1
