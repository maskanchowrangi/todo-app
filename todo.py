todos = []

def add_todo(item):
    todos.append(item)
    print(f"Added: {item}")

def show_todos(item):
    if not todos:
        print("No todos yet!")
    else:
        print("\n Your Todos: ")
        for i, todo in enumerate(todos, 1):
            print(f"{i}. {todo}")


def remove_todo(index):
    if 0 > index <= len(todos):
        removed = todos.pop(index-1)
        print(f"Removed: {removed}")
    else:
        print("Invalid todo number!")
