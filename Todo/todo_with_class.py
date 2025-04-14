import json

FILENAME = "todo.json"

tasks = []

class Task:
    def __init__(self, description, priority="Low"):
        self.description = description
        self.completed = False
        self.priority = priority

def load_tasks():
    global tasks
    try:
        with open(FILENAME, "r") as file:
            data = json.load(file)
            tasks = []
            for task in data:
                description = task["description"]
                priority = task["priority"]
                tasks.append(Task(description, priority))
    except:
        tasks = []
            
def save_tasks():
    global tasks
    with open(FILENAME, "w") as file:
        task_list = []
        for task in tasks:
            task_list.append(task.__dict__)
        json.dump(task_list, file)

def add_task():
    task_description = input("Enter task description-")
    priority = input("Enter priority(High or Medium or Low)-")
    task = Task(task_description, priority)
    tasks.append(task)
    save_tasks()

def view_tasks():
    if not tasks:
        print("No tasks found")
    else:
        for index, task in enumerate(tasks):
            if task.completed == True:
                status = "[X]"
            else:
                status = "[ ]"
            print(f"TASK {index + 1}: {status} {task.description} {task.priority}")

def mark_complete():
    index = int(input("Enter the index of task you want to mark as complete-")) - 1
    if index>= 0 and index< len(tasks):
        tasks[index].completed = True
        save_tasks()
    else:
        print("Invalid index.")

def delete_task():
    index = int(input("Enter the index of task you want to delete-")) - 1
    if index>= 0 and index< len(tasks):
        tasks.pop(index)
        save_tasks()
    else:
        print("Invalid index")

def search_task():
    keyword = input("Enter any keyword-").lower()
    found = False
    for i, task in enumerate(tasks):
        if keyword in task.description.lower():
            found = True
            if task.description:
                status = "[X]"
            else:
                status = "[ ]"
            print(f"TASK {i + 1}: {status} {task.description} {task.priority})")
    if not found:
        print("task not found")
        
def main():
    load_tasks()
    while True:
        print("!!-----TO DO LIST-----!!")
        print("1. Add task ")
        print("2. View tasks ")
        print("3. Mark task as complete ")
        print("4. Delete task ")
        print("5. Search task ")
        print("6. Exit ")

        choice = input("Enter the choice-")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            search_task()
        elif choice == "6":
            print("Exiting")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
