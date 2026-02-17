FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Reads the todos text file and returns a list of todo items.

    Args:
        filepath (str): Path to the todos file.

    Returns:
        list: List of todo strings.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Writes the list of todos into the text file.

    Args:
        todos_arg (list): List of todo items.
        filepath (str): Path to the todos file.
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)