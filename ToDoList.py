class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = int(priority)  # Ensure priority is an integer

    def __repr__(self):
        return f"Priority {self.priority}: {self.description}"

def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(f"{task.description},{task.priority}\n")

def load_tasks(filename):
    tasks = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                description, priority = line.strip().split(',')
                tasks.append(Task(description, priority))
    except FileNotFoundError:
        # File doesn't exist yet
        pass
    return tasks

def add_task(tasks, description, priority):
    tasks.append(Task(description, priority))
    tasks.sort(key=lambda t: t.priority)

def edit_task(tasks, old_description, new_description, new_priority):
    for task in tasks:
        if task.description == old_description:
            task.description = new_description
            task.priority = int(new_priority)
            tasks.sort(key=lambda t: t.priority)
            return
    print("Task not found!")

def list_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
    for task in tasks:
        print(task)

def main():
    filename = 'tasks.txt'
    tasks = load_tasks(filename)

    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. List Tasks")
        print("4. Save and Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            priority = input("Enter task priority (integer): ")
            add_task(tasks, description, priority)
        elif choice == '2':
            old_description = input("Enter the description of the task to edit: ")
            new_description = input("Enter new task description: ")
            new_priority = input("Enter new task priority (integer): ")
            edit_task(tasks, old_description, new_description, new_priority)
        elif choice == '3':
            list_tasks(tasks)
        elif choice == '4':
            save_tasks(filename, tasks)
            print("Tasks saved. Exiting.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
