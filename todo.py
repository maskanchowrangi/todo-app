import json
todos = []

def add_todo(item):
    todo = {"task": item, "done": False}
    todos.append(todo)
    print(f"Added: {item}")

def show_todos():
    if not todos:
        print("No todos yet!")
    else:
        print("\n Your Todos: ")
        for i, todo in enumerate(todos, 1):
            status = "[DONE]" if todo["done"] else "[TODO]"
            print(f"{i}. {status} {todo['task']}")

def complete_todo(index):
    if 0 < index <= len(todos):
        todos[index - 1]["done"] = True
        print(f"Completed: {todos[index - 1]['task']}")
    else:
        print("Invalid todo number!")

def remove_todo(index):
    if 0 < index <= len(todos):
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

add_todo("Learn Git")
add_todo("Build projects")
add_todo("Master python")

show_todos()

complete_todo(1)

show_todos()

# save todos when in program

save_todos() 

# interactive menu
while True:
    print("\n === Todo app ===")
    print("1. Show todos")
    print("2. Add todo")
    print("3. Complete todos")
    print("4. Remove todos")
    print("5. Quit")

    choice = input("Choice: ")

    if choice == "1":
        show_todos()
    elif choice == "2":
        task = input("Enter task: ")
        add_todo(task)
    elif choice == "3":
        show_todos()
        num = int(input("Complete which?: "))
        complete_todo(num)
    elif choice == "4":
        show_todos()
        num_r = int(input("Remove which?: "))
        remove_todo(num_r)
    elif choice.lower == "5":
        save_todos()
        print("goodbye!")
        break