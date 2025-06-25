import os

TASK_FILE= 'tasks.txt'

# Loading
def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE,'r') as file:
        return[line.strip() for line in file.readlines()]
    
# Saving
def save_tasks(tasks):
    with open(TASK_FILE,"w") as file:
        for task in tasks:
            file.write(task+'\n')

# Display Tasks
def display_tasks(tasks):
    if not tasks:
        print("No task found.")
    else:
        print("Your tasks are:\n")
        i=1
        for task in tasks:
            print(str(i),'. ',task)
            i+=1

# Add a new task
def add_task(tasks):
    task = input("Enter the task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully!")


#Remove Tasks
def remove_task(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Enter task number to remove: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            save_tasks(tasks)
            print(f"Task '{removed}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main CLI loop
def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
