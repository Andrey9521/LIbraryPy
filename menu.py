import books
import UserWork

def main_menu():
    UserWork.load_users_from_file()
    while True:
        print("\nMain Menu:")
        print("1. User Login")
        print("2. Admin Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            user = UserWork.user_login()
            if user:
                while True:
                    print(f"\nWelcome, {user['name']}!")
                    print("1. View all books")
                    print("2. Find a book")
                    print("3. Borrow a book")
                    print("4. Return a book")
                    print("5. Logout")

                    choice = input("Select an option: ")

                    if choice == '1':
                        books.Books.bookShow()
                    elif choice == '2':
                        books.Books.bookFind()
                    elif choice == '3':
                        book_name = input("Enter the name of the book you want to borrow: ")
                        UserWork.add_book_to_user(user['name'], book_name)
                    elif choice == '4':
                        UserWork.removeBookForUser(user)
                    elif choice == '5':
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice, please try again.")


        elif choice == '2':
            if UserWork.admin_login():
                while True:
                    print("\nAdmin Menu:")
                    print("1. Show all users")
                    print("2. Add a new user")
                    print("3. Delete a user")
                    print("4. View all books")
                    print("5. Add a new book")
                    print("6. Delete a book")
                    print("7. Edit a book")
                    print("8. Delete all books")
                    print("9. Exit")

                    admin_menu_choice = input("Enter your choice: ")

                    if admin_menu_choice == '1':
                        UserWork.show_users()
                    elif admin_menu_choice == '2':
                        name = input("Enter user name: ")
                        while True:
                            try:
                                user_id = int(input("Enter user ID: "))
                                break
                            except Exception:
                                print("Enter a number for ID")
                        password = input("Enter user password: ")
                        UserWork.add_user(name, user_id, password)
                    elif admin_menu_choice == '3':
                        user_id = input("Enter user ID to delete: ")
                        UserWork.delete_user(user_id)
                    elif admin_menu_choice == '4':
                        books.Books.bookShow()
                    elif admin_menu_choice == '5':
                        title = input("Enter book title: ")
                        author = input("Enter book author: ")
                        genre = input("Enter book genre: ")
                        year_of_pub = input("Enter year of publication: ")
                        availability = "available"
                        new_book = books.Books(title, author, genre, year_of_pub, availability)
                        new_book.bookCreate()
                    elif admin_menu_choice == '6':
                        title = input("Enter book title to delete: ")
                        books.Books.bookDel(title)
                    elif admin_menu_choice == '7':
                        title = input("Enter book title to edit: ")
                        new_author = input("Enter new author (leave blank to keep current): ")
                        new_genre = input("Enter new genre (leave blank to keep current): ")
                        new_year = input("Enter new year (leave blank to keep current): ")
                        books.Books.bookEdit(title, new_author, new_genre, new_year)
                    elif admin_menu_choice == '8':
                        books.Books.bookDelAll()
                    elif admin_menu_choice == '9':
                        print("Exiting admin menu...")
                        break
                    else:
                        print("Invalid choice, please try again.")

        elif choice == '3':
            print("Exiting the program...")
            break

        else:
            print("Invalid choice, please try again.")
