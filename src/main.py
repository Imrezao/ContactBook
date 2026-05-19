"""
Author: Reza Omidi
Date Created: 5/6/2025
"""
from contact_book import contactbook


if __name__ == "__main__":
    book = contactbook()

    while True:
        print("1. Add contact")
        print("2. Edit contact")
        print("3. View contacts")
        print("4. Delete contact")
        print("5. Quit")
        user_choice = input("\nPlease choose an option: ")

        if user_choice == '1':
            name = input("\nEnter Contact name: ")
            phone = input("Enter Contact phone: ")
            email = input("Enter Contact email: ")
            address = input("Enter Contact address: ")
            book.add_contact(name, phone, email, address)

        elif user_choice == '2':
            name = input("\nEnter name of the contact to edit: ")
            phone = input("Enter new/updated phone number or press Enter to keep unchanged: ")
            email = input("Enter new/updated email or press Enter to keep unchanged: ")
            address = input("Enter new/updated address or press Enter to keep unchanged: ")
            book.update_contact(name, phone or None, email or None, address or None)

        elif user_choice == '3':
            print("\nList of Contacts:")
            book.view_contacts()

        elif user_choice == '4':
            name = input("\nEnter name of contact to delete: ")
            book.delete_contact(name)
            print('-'*50)
            

        elif user_choice == '5':
            print("\nThank You for using Contact Book Application. Goodbye!")
            break

        else:
            print("\nInvalid choice! Please try again.")
