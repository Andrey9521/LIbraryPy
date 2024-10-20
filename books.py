import os


class Books:
    def __init__(self, title, author, genre, year_of_pub, availability):
        self.title = title
        self.author = author
        self.genre = genre
        self.year_of_pub = year_of_pub
        self.availability = availability

    def bookCreate(self):
        try:
            with open("books.txt", "a") as file:
                file.write(f"{self.title},{self.author},{self.genre},{self.year_of_pub},{self.availability}\n")
            print(f"Book '{self.title}' created successfully.")
        except Exception as e:
            print(f"Error creating book: {e}")

    @staticmethod
    def bookShow():
        if os.path.exists("books.txt"):
            try:
                with open("books.txt", "r") as file:
                    booksList = file.readlines()
                if not booksList:
                    print("No books available.")
                    return

                for i, book in enumerate(booksList, 1):
                    elements = book.strip().split(",")
                    book_name = elements[0].strip()
                    author = elements[1].strip()
                    genre = elements[2].strip()
                    yob = elements[3].strip()
                    afb = elements[4].strip()
                    print(
                        f"Book {i}:\n\tName: {book_name}\n\tAuthor: {author}\n\tGenre: {genre}\n\tYear of publication: {yob}\n\tAccess for borrow: {afb}\n")
            except Exception as e:
                print(f"Error reading books: {e}")
        else:
            print("No books available.")

    @staticmethod
    def bookDel(title):
        try:
            if os.path.exists("books.txt"):
                with open("books.txt", "r") as file:
                    lines = file.readlines()

                book_found = False

                with open("books.txt", "w") as file:
                    for line in lines:
                        if line.split(',')[0].strip().lower() != title.strip().lower():
                            file.write(line)
                        else:
                            book_found = True

                if book_found:
                    print(f"Book '{title}' deleted successfully.")
                else:
                    print(f"No book with title '{title}' found.")
            else:
                print("No books to delete.")
        except Exception as e:
            print(f"Error deleting book: {e}")

    @staticmethod
    def bookEdit(title, new_author=None, new_genre=None, new_year=None):
        try:
            if os.path.exists("books.txt"):
                with open("books.txt", "r") as file:
                    books = file.readlines()
                with open("books.txt", "w") as file:
                    for book in books:
                        book_data = book.strip().split(',')
                        if book_data[0] == title:
                            book_data[1] = new_author or book_data[1]
                            book_data[2] = new_genre or book_data[2]
                            book_data[3] = new_year or book_data[3]
                            book_data[4] = book_data[4]
                            file.write(','.join(book_data) + '\n')
                            print(f"Book '{title}' edited successfully.")
                        else:
                            file.write(book)
            else:
                print("No books available to edit.")
        except Exception as e:
            print(f"Error editing book: {e}")

    @staticmethod
    def bookDelAll():
        try:
            if os.path.exists("books.txt"):
                os.remove("books.txt")
                print("All books deleted successfully.")
            else:
                print("No books available to delete.")
        except Exception as e:
            print(f"Error deleting all books: {e}")

    @staticmethod
    def bookFind():
        name = input("Enter a characteristic of the book you want to find: ")
        try:
            with open("books.txt", "r") as books:
                booksList = books.readlines()
        except FileNotFoundError:
            print("File not found, create a new file!")
            return

        foundBooks = []
        for book in booksList:
            elements = book.strip().split(",")
            book_name = elements[0].strip()
            author = elements[1].strip()
            genre = elements[2].strip()
            yob = elements[3].strip()
            afb = elements[4].strip()
            if name.lower() in (book_name.lower(), author.lower(), genre.lower(), str(yob), afb.lower()):
                foundBooks.append((book_name, author, genre, yob, afb))

        if not foundBooks:
            print(f"No book found with the characteristic: '{name}'")
        else:
            for i, book in enumerate(foundBooks, 1):
                print(
                    f"Found Book {i}:\n\tName: {book[0]}\n\tAuthor: {book[1]}\n\tGenre: {book[2]}\n\tYear of publication: {book[3]}\n\tAccess for borrow: {book[4]}")

    def __del__(self):
        print(f"Book '{self.title}' is being deleted.")
