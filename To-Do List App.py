import json
import os

class TodoApp:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    # Load tasks from file
    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        return []

    # Save tasks to file
    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    # Add a new task
    def add_task(self, task):
        self.tasks.append({
            "task": task,
            "done": False
        })
        self.save_tasks()
        print("Task added successfully!")

    # View all tasks
    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return

        for i, task in enumerate(self.tasks, start=1):
            status = "✔" if task["done"] else "✖"
            print(f"{i}. [{status}] {task['task']}")

    # Mark task as done
    def mark_done(self, index):
        try:
            self.tasks[index]["done"] = True
            self.save_tasks()
            print("Task marked as done!")
        except IndexError:
            print("Invalid task number.")

    # Delete a task
    def delete_task(self, index):
        try:
            removed = self.tasks.pop(index)
            self.save_tasks()
            print(f"Deleted task: {removed['task']}")
        except IndexError:
            print("Invalid task number.")


def main():
    app = TodoApp()

    while True:
        print("\n===== TO-DO LIST =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task: ")
            app.add_task(task)

        elif choice == "2":
            app.view_tasks()

        elif choice == "3":
            app.view_tasks()
            index = int(input("Enter task number to mark done: ")) - 1
            app.mark_done(index)

        elif choice == "4":
            app.view_tasks()
            index = int(input("Enter task number to delete: ")) - 1
            app.delete_task(index)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()