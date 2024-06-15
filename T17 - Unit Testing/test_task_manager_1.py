import unittest
import io
import unittest.mock

# Task class representing individual tasks
class Task:
    def __init__(self, task_id, title, description):
        self.task_id = task_id
        self.title = title
        self.description = description

# TaskManager class managing tasks
class TaskManager:
    def __init__(self):
        self.tasks = []

    # Method to add a task to the task list
    def add_task(self, task):
        self.tasks.append(task)

    # Method to remove a task from the task list
    def remove_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]

    # Method to display all tasks
    def display_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        print("Tasks:")
        for task in self.tasks:
            print(f"ID: {task.task_id}, Title: {task.title}, Description: {task.description}")

# Unit tests for the TaskManager class
class TestTaskManager(unittest.TestCase):
    # Setup method to initialize a TaskManager instance before each test
    def setUp(self):
        self.task_manager = TaskManager()

    # Test case to check the add_task method
    def test_add_task(self):
        task1 = Task(1, "Task 1", "Description for Task 1")
        self.task_manager.add_task(task1)
        self.assertEqual(len(self.task_manager.tasks), 1)

    # Test case to check the remove_task method
    def test_remove_task(self):
        task1 = Task(1, "Task 1", "Description for Task 1")
        task2 = Task(2, "Task 2", "Description for Task 2")
        self.task_manager.add_task(task1)
        self.task_manager.add_task(task2)
        self.task_manager.remove_task(1)
        self.assertEqual(len(self.task_manager.tasks), 1)
        self.assertNotIn(task1, self.task_manager.tasks)

    # Test case to check the display_tasks method
    def test_display_tasks(self):
        task1 = Task(1, "Task 1", "Description for Task 1")
        task2 = Task(2, "Task 2", "Description for Task 2")
        self.task_manager.add_task(task1)
        self.task_manager.add_task(task2)

        expected_output = "Tasks:\nID: 1, Title: Task 1, Description: Description for Task 1\nID: 2, Title: Task 2, Description: Description for Task 2\n"
        
        # Redirecting stdout to StringIO object to capture printed output
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.task_manager.display_tasks()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

# Main entry point to run unit tests
if __name__ == '__main__':
    unittest.main()
