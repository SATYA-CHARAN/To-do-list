import csv
from tabulate import tabulate
from datetime import datetime

class TodoApp:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                reader = csv.DictReader(file)
                tasks = [task for task in reader]
            return tasks
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.filename, 'w', newline='') as file:
            fieldnames = ['Task', 'Priority', 'Due Date', 'Completed']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for task in self.tasks:
                writer.writerow(task)

    def list_tasks(self):
        print(tabulate(self.tasks, headers="keys"))

    def add_task(self, task, priority, due_date):
        self.tasks.append({
            'Task': task,
            'Priority': priority,
            'Due Date': due_date,
            'Completed': 'No'
        })
        self.save_tasks()
        print("Task added successfully.")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            task = self.tasks.pop(task_index)
            self.save_tasks()
            print(f"Task '{task['Task']}' removed.")
        else:
            print("Invalid task index.")

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['Completed'] = 'Yes'
            self.save_tasks()
            print(f"Task '{self.tasks[task_index]['Task']}' marked as completed.")
        else:
            print("Invalid task index.")

def main():
    filename = 'tasks.csv'
    todo_app = TodoApp(filename)

    while True:
        print("\nTodo List Application")
        print("1. List tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Mark task as completed")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            todo_app.list_tasks()
        elif choice == '2':
            task = input("Enter task: ")
            priority = input("Enter priority (High/Medium/Low): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            todo_app.add_task(task, priority, due_date)
        elif choice == '3':
            task_index = int(input("Enter the task index to remove: "))
            todo_app.remove_task(task_index)
        elif choice == '4':
            task_index = int(input("Enter the task index to mark as completed: "))
            todo_app.mark_task_completed(task_index)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
