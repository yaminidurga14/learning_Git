# simple_task_manager.py

tasks = []

def show_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")