# todo_list.py

# Class to manage the to-do list
class ToDoList:
    def __init__(self):
        # Initialize an empty list to store tasks
        self.tasks = []

    # Add a task to the list
    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Added task: '{task}'")

    # Remove a task by index
    def remove_task(self, index):
        try:
            removed_task = self.tasks.pop(index)
            print(f"Removed task: '{removed_task['task']}'")
        except IndexError:
            print("Invalid task number.")

    # Mark a task as completed
    def complete_task(self, index):
        try:
            self.tasks[index]["completed"] = True
            print(f"Marked task '{self.tasks[index]['task']}' as completed.")
        except IndexError:
            print("Invalid task number.")

    # Edit a task's description
    def edit_task(self, index, new_task):
        try:
            self.tasks[index]["task"] = new_task
            print(f"Updated task {index + 1} to: '{new_task}'")
        except IndexError:
            print("Invalid task number.")

    # View all tasks
    def view_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                status = "Completed" if task["completed"] else "Not Completed"
                print(f"{i}. {task['task']} [{status}]")

# Function to display menu
def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Remove a task")
    print("4. Mark a task as completed")
    print("5. Edit a task")
    print("6. Exit")

# Main function to run the application
def main():
    todo_list = ToDoList()  # Create an instance of ToDoList

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            # View all tasks
            todo_list.view_tasks()

        elif choice == '2':
            # Add a new task
            task = input("Enter the task description: ")
            todo_list.add_task(task)

        elif choice == '3':
            # Remove a task
            try:
                index = int(input("Enter the task number to remove: ")) - 1
                todo_list.remove_task(index)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '4':
            # Mark a task as completed
            try:
                index = int(input("Enter the task number to mark as completed: ")) - 1
                todo_list.complete_task(index)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '5':
            # Edit a task
            try:
                index = int(input("Enter the task number to edit: ")) - 1
                new_task = input("Enter the new task description: ")
                todo_list.edit_task(index, new_task)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '6':
            # Exit the application
            print("Exiting the To-Do List Application. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose an option from 1 to 6.")

if __name__ == "__main__":
    main()
