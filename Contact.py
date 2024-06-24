contacts = []
def display_menu():
    print("Welcome to Contact System")
    print("Choose an option:")
    print("1. Add new contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Delete a contact")
    print("5. Exit")
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    contacts.append(contact)
    print("Contact added successfully!")
def view_contacts():
    if not contacts:
        print("No contacts")
    else:
        for contact in contacts:
            print("\nName:", contact['name'])
            print("Phone:", contact['phone'])
            print("Email:", contact['email'])
            print("Address:", contact['address'])
            print("-" * 20)
def search_contact():
    if not contacts:
        print("No contacts to search")
        return
      name = input("Enter name to search: ")
    found = False
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print("\nName:", contact['name'])
            print("Phone:", contact['phone'])
            print("Email:", contact['email'])
            print("Address:", contact['address'])
            found = True
            break
    if not found:
        print("Contact not found")
def delete_contact():
    if not contacts:
        print("No contacts to delete")
        return
    name = input("Enter name to delete: ")
    found = False
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully!")
            found = True
            break
    if not found:
        print("Contact not found")
while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
      
