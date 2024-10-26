contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print(f"Contact '{name}' added.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

def main():
    while True:
        print("\n1. Add Contact")
        print("2. View Contacts")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            add_contact(name, phone)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
