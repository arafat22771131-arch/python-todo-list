
import json
from pathlib import Path

# Task data will be saved in this file
DATA_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    """Load tasks from the JSON file."""
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read saved tasks.")
        return []


def save_tasks(tasks):
    """Save tasks to the JSON file."""
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4, ensure_ascii=False)
    except OSError:
        print("Error: Could not save tasks.")


def show_tasks(tasks):
    """Display all tasks."""
    print("\n===== YOUR TO-DO LIST =====")

    if not tasks:
        print("No tasks yet. Add your first task!")
        return

    for number, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f'{number}. [{status}] {task["title"]}')


def add_task(tasks):
    """Add a new task."""
    title = input("Enter your task: ").strip()

    if not title:
        print("Task cannot be empty!")
        return

    tasks.append({
        "title": title,
        "completed": False
    })

    save_tasks(tasks)
    print("Task added successfully!")


def complete_task(tasks):
    """Mark a task as completed."""
    show_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Enter task number to complete: "))
    except ValueError:
        print("Please enter a valid number!")
        return

    if 1 <= number <= len(tasks):
        tasks[number - 1]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    else:
        print("Invalid task number!")


def delete_task(tasks):
    """Delete a task."""
    show_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Enter task number to delete: "))
    except ValueError:
        print("Please enter a valid number!")
        return

    if 1 <= number <= len(tasks):
        removed = tasks.pop(number - 1)
        save_tasks(tasks)
        print(f'Task deleted: {removed["title"]}')
    else:
        print("Invalid task number!")


def main():
    tasks = load_tasks()

    while True:
        print("\n===== PYTHON TO-DO LIST =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye! Your tasks are saved.")
            break
        else:
            print("Invalid choice. Please choose 1-5.")


if __name__ == "__main__":
    main()
