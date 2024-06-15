"""
task_manager_template
"""

class Task:
    def __init__(self, task_id, title, description):
        self.task_id = task_id
        self.title = title
        self.description = description

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]

    def display_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        print("Tasks:")
        for task in self.tasks:
            print(f"ID: {task.task_id}, Title: {task.title}, Description: {task.description}")

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task_id = len(task_manager.tasks) + 1
            task = Task(task_id, title, description)
            task_manager.add_task(task)
            print("Task added successfully!")

        elif choice == '2':
            task_id = int(input("Enter task ID to remove: "))
            task_manager.remove_task(task_id)
            print("Task removed successfully!")

        elif choice == '3':
            task_manager.display_tasks()

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
