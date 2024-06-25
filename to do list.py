import os

def display_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = [line.strip() for line in file]
        return tasks
    return []

tasks = load_tasks()

while True:
    print("\nTo-Do List")
    display_tasks(tasks)
    print("\nOptions:")
    print("1. Add task")
    print("2. Remove task")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        task = input("Enter a new task: ")
        tasks.append(task)
        save_tasks(tasks)
    elif choice == '2':
        task_number = int(input("Enter the task number to remove: "))
        if 0 < task_number <= len(tasks):
            tasks.pop(task_number - 1)
            save_tasks(tasks)
        else:
            print("Invalid task number.")
    elif choice == '3':
        break
    else:
        print("Invalid choice.")
