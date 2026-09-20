# SkillNexis Python Programming
# Week 2 - Assignment 1
# Contact Book using Dictionary

contacts = {}


def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")

    contacts[name] = phone
    print("Contact added successfully!")


def search_contact():
    name = input("Enter contact name to search: ")

    if name in contacts:
        print("Name:", name)
        print("Phone:", contacts[name])
    else:
        print("Contact not found.")


def update_contact():
    name = input("Enter contact name to update: ")

    if name in contacts:
        phone = input("Enter new phone number: ")
        contacts[name] = phone
        print("Contact updated successfully!")
    else:
        print("Contact not found.")


def delete_contact():
    name = input("Enter contact name to delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")


def display_contacts():
    if not contacts:
        print("Contact book is empty.")
    else:
        print("\n===== CONTACT BOOK =====")
        for name, phone in contacts.items():
            print("Name:", name, "| Phone:", phone)


print("================================")
print("          CONTACT BOOK")
print("================================")

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        search_contact()

    elif choice == "3":
        update_contact()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        display_contacts()

    elif choice == "6":
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice. Please try again.")