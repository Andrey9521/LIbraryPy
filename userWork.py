import os


class User:
    def __init__(self, name, user_id, password, list_of_books=None):
        self.name = name
        self.id = user_id
        self.password = password
        self.list_of_books = list_of_books if list_of_books is not None else []

    def add_to_list(self, users_list):
        user_dict = {
            "name": self.name,
            "id": self.id,
            "password": self.password,
            "list_of_books": self.list_of_books
        }
        users_list.append(user_dict)
        save_users_to_file(users_list)

    def show_user_info(self):
        print(f"Name: {self.name}, ID: {self.id}, Books: {', '.join(self.list_of_books)}")

    def clear(self):
        self.list_of_books.clear()
        print(f"Cleared books for user '{self.name}'.")


users_list = []


def save_users_to_file(users_list):
    try:
        with open("users.txt", "w") as file:
            for user in users_list:
                file.write(f"{user['name']},{user['id']},{user['password']},{','.join(user['list_of_books'])}\n")
        print("Users saved successfully.")
    except Exception as e:
        print(f"Error saving users: {e}")


def load_users_from_file():
    if os.path.exists("users.txt"):
        try:
            with open("users.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(',')
                    name, user_id, password = parts[:3]
                    list_of_books = parts[3:] if len(parts) > 3 else []
                    users_list.append({
                        "name": name,
                        "id": user_id,
                        "password": password,
                        "list_of_books": list_of_books
                    })
            print("Users loaded successfully.")
        except Exception as e:
            print(f"Error loading users: {e}")
    else:
        print("No users found.")


def show_users():
    if not users_list:
        print("No users found.")
    else:
        print("List of users:")
        for user in users_list:
            print(f"Name: {user['name']}, ID: {user['id']}, Books: {', '.join(user['list_of_books'])}")


def add_user(name, user_id, password):
    user = User(name, user_id, password)
    user.add_to_list(users_list)
    print(f"User '{name}' added successfully.")


def delete_user(user_id):
    global users_list
    try:
        if os.path.exists("users.txt"):
            with open("users.txt", "r") as file:
                users = file.readlines()

            user_found = False

            with open("users.txt", "w") as file:
                for user in users:
                    if user.split(',')[1] != user_id:
                        file.write(user)
                    else:
                        user_found = True
                        users_list = [u for u in users_list if u['id'] != user_id]

            if user_found:
                print(f"User with ID '{user_id}' deleted successfully.")
            else:
                print(f"No user found with ID '{user_id}'.")
        else:
            print("No users to delete.")
    except Exception as e:
        print(f"Error deleting user: {e}")


def add_book_to_user(user_name, book_name):
    user_found = next((user for user in users_list if user['name'].lower() == user_name.lower()), None)

    if user_found is None:
        print(f"No user found with name '{user_name}'")
        return

    if not os.path.exists("books.txt"):
        print("Books file not found.")
        return

    try:
        with open("books.txt", "r") as books_file:
            books_show = books_file.readlines()
    except Exception as e:
        print(f"Error reading books: {e}")
        return

    if not books_show:
        print("No books available.")
        return

    for i, book in enumerate(books_show):
        elements = book.strip().split(",")
        name = elements[0].strip()
        afb = elements[4].strip()
        if book_name.lower() == name.lower() and afb.lower() == "available":
            elements[4] = f"borrowed by {user_name}"
            user_found['list_of_books'].append(book_name)
            books_show[i] = ','.join(elements) + "\n"
            save_users_to_file(users_list)
            with open("books.txt", "w") as books_file:
                books_file.writelines(books_show)
            print(f"Book '{book_name}' has been borrowed by {user_name}")
            return
    print(f"Book '{book_name}' is not available for borrowing.")


def removeBookForUser(user_found):
    bookName = input("Enter book name to return: ")
    print("User's borrowed books:", user_found['list_of_books'])

    if bookName not in user_found['list_of_books']:
        print(f"User '{user_found['name']}' does not have the book '{bookName}'")
        return

    if not os.path.exists("books.txt"):
        print("Books file not found.")
        return

    try:
        with open("books.txt", "r+", encoding='utf-8') as books:
            booksShow = books.readlines()
    except Exception as e:
        print(f"Error reading books: {e}")
        return

    for i, book in enumerate(booksShow):
        elements = book.strip().split(",")
        if len(elements) < 5:
            continue
        name = elements[0].strip()
        afb = elements[4].strip()

        if bookName.lower() == name.lower() and afb.lower() == f"borrowed by {user_found['name'].lower()}":
            elements[4] = "available"
            booksShow[i] = f"{elements[0]},{elements[1]},{elements[2]},{elements[3]},{elements[4]}\n"
            user_found['list_of_books'].remove(bookName)
            save_users_to_file(users_list)
            with open("books.txt", "w", encoding='utf-8') as books:
                books.writelines(booksShow)
            print(f"Book '{bookName}' has been returned by {user_found['name']}")
            return

    print(f"Book '{bookName}' was not found among borrowed books.")


def user_login():
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    for user in users_list:
        if user['name'] == name and user['password'] == password:
            return user
    print("Invalid username or password.")
    return None


def admin_login():
    admin_name = "admin"
    admin_password = "admin"
    name = input("Enter admin name: ")
    password = input("Enter admin password: ")
    if name == admin_name and password == admin_password:
        return True
    print("Invalid admin credentials.")
    return False
