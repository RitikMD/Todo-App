from sqlmodel import Field, SQLModel, create_engine, Session, select

#connection 
DB_URL = "mysql+mysqlconnector://root:Ritik%40123@127.0.0.1:3306/todo"
engine = create_engine(DB_URL, echo=True)

class Task(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    description: str
    completed: bool= False
    priority: str= "Low"

def create_tables():
    SQLModel.metadata.create_all(engine)

def add_task():
    task_desc = input("Enter task description-")
    priority = input("Enter priority (High or Medium or Low)-")
    new_task = Task(description=task_desc, priority=priority)

    with Session(engine) as session:
        session.add(new_task)
        session.commit()

def view_tasks():
    with Session(engine) as session:
        tasks = session.exec(select(Task)).all()
        if not tasks:
            print("Tasks not found")
        else:
            for index, task in enumerate(tasks):
                if task.completed == True:
                    status = "[x]" 
                else:
                    status = "[ ]"
                print(f"TASK {index + 1}: {status} {task.description} ({task.priority})")

def mark_complete():
    index = int(input("Enter task number to mark as complete-")) - 1
    with Session(engine) as session:
        tasks = session.exec(select(Task)).all()
        if index>=0 and index<len(tasks):
            task = tasks[index]
            task.completed = True
            session.add(task)
            session.commit()
        else:
            print("Invalid task number")

def mark_incomplete():
    index = int(input("Enter task number to mark as incomplete-")) - 1
    with Session(engine) as session:
        tasks = session.exec(select(Task)).all()
        if index>=0 and index<len(tasks):
            task = tasks[index]
            task.completed = False
            session.add(task)
            session.commit()
        else:
            print("Invalid task number")

def delete_task():
    index = int(input("Enter task number to delete:")) - 1
    with Session(engine) as session:
        tasks = session.exec(select(Task)).all()
        if index>=0 and index<len(tasks):
            session.delete(tasks[index])
            session.commit()
        else:
            print("Invalid task number")

def search_task():
    keyword = input("Enter keyword to search the task-").lower()
    with Session(engine) as session:
        statement = select(Task).where(Task.description.ilike(f"%{keyword}%"))
        results = session.exec(statement).all()
        if results:
            for i, task in enumerate(results):
                if task.completed == True:
                    status = "[x]" 
                else:
                    status = "[ ]"
                print(f"TASK {i + 1}: {status} {task.description} ({task.priority})")
        else:
            print("Task not found")

def main():
    create_tables()
    while True:
        print("!!-----TO DO LIST-----!!")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as complete")
        print("4. Mark task as incomplete")
        print("5. Delete task")
        print("6. Search task")
        print("7. Exit")

        choice = input("Enter your choice-")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            mark_incomplete()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            search_task()
        elif choice == "7":
            print("Exiting")
            print("Exited")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
