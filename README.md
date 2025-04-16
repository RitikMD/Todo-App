
# To-Do List Application

A simple To-Do list application built using **SQLModel** and **MySQL**. The application allows you to add, view, mark tasks as complete/incomplete, delete tasks, and search tasks.

## Features

- **Add a task**: Allows you to add a new task with a description and priority.
- **View tasks**: Displays a list of all tasks with their status (completed or not).
- **Mark task as complete/incomplete**: Allows you to update the completion status of a task.
- **Delete task**: Allows you to delete a specific task by its index.
- **Search task**: Allows you to search for tasks containing a keyword in their description.

## Requirements

- Python 3.6 or higher
- MySQL database
- `sqlmodel` library
- `mysql-connector-python` library

You can install the required libraries by running:

```bash
pip install sqlmodel mysql-connector-python
```

## Setup

1. **Database Connection**:
   - The application connects to a MySQL database at `127.0.0.1:3306` with the username `your username` and password `your password`. The database is named `your database name`.
   - If the database does not exist, you may need to create it manually, or the application will handle table creation when it runs.

2. **Create Tables**:
   - The `create_tables` function ensures the `Task` table is created automatically when the script runs.

## Code Overview

### Task Model

The `Task` model represents a task in the to-do list. It has the following attributes:
- `id`: The unique identifier for each task.
- `description`: A text field for the task description.
- `completed`: A boolean indicating whether the task is completed or not.
- `priority`: A string to set the priority of the task, with default as "Low".

### Functions

- **create_tables()**: Creates the necessary tables in the database if they don’t exist.
- **add_task()**: Prompts the user to enter a task description and priority, then adds it to the database.
- **view_tasks()**: Displays all tasks, showing their completion status and priority.
- **mark_complete()**: Allows the user to mark a task as complete by entering its index.
- **mark_incomplete()**: Allows the user to mark a task as incomplete by entering its index.
- **delete_task()**: Allows the user to delete a task by entering its index.
- **search_task()**: Prompts the user for a keyword and searches for tasks that contain that keyword in their description.

### Main Loop

The `main()` function starts a loop where the user can choose from the following options:
1. Add a new task.
2. View all tasks.
3. Mark a task as complete.
4. Mark a task as incomplete.
5. Delete a task.
6. Search for a task.
7. Exit the application.

The application will keep running until the user chooses to exit.

## Example Usage

Run the script to interact with the to-do list:

```bash
python todo_list.py
```

The program will prompt you to select an action by entering the corresponding number:

```
!!-----TO DO LIST-----!!
1. Add task
2. View tasks
3. Mark task as complete
4. Mark task as incomplete
5. Delete task
6. Search task
7. Exit
```

You can then follow the on-screen prompts to add, view, mark, delete, or search for tasks.

## License

This project is open-source and available under the MIT License.
