todos = []

def add_todo(item):
    todos.append(item)
    print(f"Added: {item}")

def show_todos(item):
    for i, todo in enumerate(todos, 1):
        print(f"{i}. {todo}")

add_todo("Learn Git")
add_todo("Build projects")
show_todos()
