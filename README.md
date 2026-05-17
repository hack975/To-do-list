# Python To-Do List Application

A simple and efficient command-line To-Do List application built with Python. This project allows users to manage daily tasks by adding, viewing, completing, and deleting tasks with persistent storage using JSON.

---

## Features

* Add new tasks
* View all tasks
* Mark tasks as completed
* Delete tasks
* Persistent task storage using JSON
* Simple and beginner-friendly CLI interface
* Automatic file handling

---

## Technologies Used

* Python 3
* JSON
* OS Module

---

## How It Works

The application stores tasks in a local `tasks.json` file. Each task contains:

* Task description
* Completion status

When the program starts, it automatically loads saved tasks. Any changes made are instantly saved to the JSON file.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/python-todo-app.git
```

Navigate into the project directory:

```bash
cd python-todo-app
```

Run the application:

```bash
python todo.py
```

---

## Example Usage

### Main Menu

```bash
===== TO-DO LIST =====
1. Add Task
2. View Tasks
3. Mark Task as Done
4. Delete Task
5. Exit
```

### Example Tasks

```bash
1. [✖] Complete Python project
2. [✔] Study networking basics
3. [✖] Push code to GitHub
```

---

## Project Structure

```bash
python-todo-app/
│
├── todo.py
├── tasks.json
└── README.md
```

---

## Code Highlights

### Task Persistence

Tasks are automatically saved using JSON:

```python
json.dump(self.tasks, file, indent=4)
```

### Completion Tracking

Each task stores its completion status:

```python
{
    "task": "Finish assignment",
    "done": False
}
```

---

## Educational Purpose

This project is ideal for learning:

* Python file handling
* JSON data storage
* Object-Oriented Programming (OOP)
* CLI application development
* Basic CRUD operations

---

## Future Improvements

* Task deadlines and reminders
* Priority levels
* Search functionality
* GUI version using Tkinter or PyQt
* User authentication
* Cloud synchronization
* Colored terminal interface


---

## Author

Developed by [mpho mudau]

If you found this project useful, consider giving it a ⭐ on GitHub.
