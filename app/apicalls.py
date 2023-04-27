import requests


def get_todo_item(todo_id):
    """Make Api call for todo item by id."""
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos/{todo_id}")
    return response
