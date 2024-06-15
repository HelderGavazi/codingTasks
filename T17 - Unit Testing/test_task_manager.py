import unittest
import io
import unittest.mock
from task_manager_template import *

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.task_manager = TaskManager()

    def test_add_task(self):
        task1 = Task(1, "Task 1", "Description for Task 1")
        self.task_manager.add_task(task1)
        self.assertEqual(len(self.task_manager.tasks), 1)

    def test_remove_task(self):
        task1 = Task(1, "Task 1", "Description for Task 1")
        task2 = Task(2, "Task 2", "Description for Task 2")
        self.task_manager.add_task(task1)
        self.task_manager.add_task(task2)
        self.task_manager.remove_task(1)
        self.assertEqual(len(self.task_manager.tasks), 1)
        self.assertNotIn(task1, self.task_manager.tasks)

    def test_display_tasks(self):
        task1 = Task(1, "Task 1", "Description for Task 1")
        task2 = Task(2, "Task 2", "Description for Task 2")
        self.task_manager.add_task(task1)
        self.task_manager.add_task(task2)

        expected_output = "Tasks:\nID: 1, Title: Task 1, Description: Description for Task 1\nID: 2, Title: Task 2, Description: Description for Task 2\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.task_manager.display_tasks()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
