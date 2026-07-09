contact_numbers = {
    "khushi": "7576584584",
    "sarthak": "8475892085",
    "vansh": "7577895803"
}

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Update Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter the name: ")
        phone_number = input("Enter the number: ")

        if name in contact_numbers:
            print("Contact already exists.")
        else:
            contact_numbers[name] = phone_number
            print("Contact added successfully.")

    elif choice == "2":
        print("\n--- Contact List ---")
        for name in contact_numbers:
            print(name, ":", contact_numbers[name])

    elif choice == "3":
        search_name = input("Enter the name: ")

        if search_name in contact_numbers:
            print(search_name, ":", contact_numbers[search_name])
        else:
            print("Contact not found.")

    elif choice == "4":
        delete_name = input("Enter the name: ")

        if delete_name in contact_numbers:
            contact_numbers.pop(delete_name)
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    elif choice == "5":
        update_name = input("Enter the name: ")

        if update_name in contact_numbers:
            new_phone_number = input("Enter the new number: ")
            contact_numbers[update_name] = new_phone_number
            print("Contact updated successfully.")
        else:
            print("Contact does not exist.")

    elif choice == "6":
        print("Exiting Contact Book...")
        break

    else:
        print("Invalid choice.")