import json
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

def complete_todo(index):
    if 0 < index <= len(todos):
        todos[index - 1]["done"] = True
        print(f"Completed: {todos[index - 1]['task']}")
    else:
        print("Invalid todo number!")

def remove_todo(index):
    if 0 > index <= len(todos):
        removed = todos.pop(index-1)
        print(f"Removed: {removed}")
    else:
        print("Invalid todo number!")

def save_todos():
    with open("todos.json", "w") as f:
        json.dump(todos, f)
    print("Todos saved!")

def load_todos():
    global todos
    try:
        with open("todos.json", "r") as f:
            todos = json.load(f)
        print("Todos loaded!")
    except FileNotFoundError:
        print("No saved todos found.")

# load existing todos

load_todos()

# test the function

add_todo("Learn Git")
add_todo("Build projects")
add_todo("Master python")

show_todos()

complete_todo(1)
remove_todo(1)

show_todos()

# save todos when in program

save_todos() 