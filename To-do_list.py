tasks = []
#function to add tasks
def add_task():
    description = input("Enter task description: ")
    due_date = input("Enter due date (optional): ")
    priority = input("Enter priority (optional): ")
    task = {"description": description, "due_date": due_date, "priority": priority, "completed": False}
    tasks.append(task)
    print("Task added successfully.")

#function to display
def display_tasks():
    for idx, task in enumerate(tasks, 1):
        status = "Completed" if task["completed"] else "Not Completed"
        print(f"{idx}. Description: {task['description']}, Due Date: {task['due_date']}, Priority: {task['priority']}, Status: {status}")

#function to mark tasks as completed
def mark_completed():
    display_tasks()
    task_num = int(input("Enter task number to mark as completed: "))
    if 1 <= task_num <= len(tasks):
        tasks[task_num - 1]["completed"] = True
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

#function to update tasks
def update_task():
    display_tasks()
    task_num = int(input("Enter task number to update: "))
    if 1 <= task_num <= len(tasks):
        task = tasks[task_num - 1]
        description = input("Enter updated description (Enter to keep the same): ")
        due_date = input("Enter updated due date (Enter to keep the same): ")
        priority = input("Enter updated priority (Enter to keep the same): ")
        if description:
            task["description"] = description
        if due_date:
            task["due_date"] = due_date
        if priority:
            task["priority"] = priority
        print("Task updated successfully.")
    else:
        print("Invalid task number.")

#function to remove task
def remove_task():
    display_tasks()
    task_num = int(input("Enter the task number to remove: "))
    if 1 <= task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)
        print(f"Task '{removed_task['description']}' removed.")
    else:
        print("Invalid task number.")
        
#main loop
while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Mark Task as Completed")
    print("4. Update Task")
    print("5. Remove Task")
    print("6. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        display_tasks()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        update_task()
    elif choice == "5":
        remove_task()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
