# library/ui.py

from library.book import Book
from library.user import User
from library.author import Author

class LibraryUI:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []
        self.initialize_data()

    def initialize_data(self):
        # Adding predefined authors
        authors = [
            Author("George Orwell", "English novelist and essayist, journalist and critic."),
            Author("J.K. Rowling", "British author, best known for the Harry Potter series."),
            Author("J.R.R. Tolkien", "English writer, best known for 'The Hobbit' and 'The Lord of the Rings'."),
            Author("Harper Lee", "American novelist, best known for 'To Kill a Mockingbird'."),
            Author("F. Scott Fitzgerald", "American novelist, known for 'The Great Gatsby'."),
            Author("Jane Austen", "English novelist known for 'Pride and Prejudice'."),
            Author("Mark Twain", "American writer, best known for 'The Adventures of Tom Sawyer' and 'Huckleberry Finn'."),
            Author("J.D. Salinger", "American writer, known for 'The Catcher in the Rye'."),
            Author("Agatha Christie", "British author known for her detective novels."),
            Author("Leo Tolstoy", "Russian author, known for 'War and Peace' and 'Anna Karenina'.")
        ]
        self.authors.extend(authors)

        # Adding predefined books
        books = [
            Book("1984", "George Orwell", "Dystopian", "1949"),
            Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "Fantasy", "1997"),
            Book("The Hobbit", "J.R.R. Tolkien", "Fantasy", "1937"),
            Book("To Kill a Mockingbird", "Harper Lee", "Fiction", "1960"),
            Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic", "1925"),
            Book("Pride and Prejudice", "Jane Austen", "Romance", "1813"),
            Book("The Adventures of Tom Sawyer", "Mark Twain", "Adventure", "1876"),
            Book("The Catcher in the Rye", "J.D. Salinger", "Fiction", "1951"),
            Book("Murder on the Orient Express", "Agatha Christie", "Mystery", "1934"),
            Book("War and Peace", "Leo Tolstoy", "Historical Fiction", "1869")
        ]
        self.books.extend(books)

    def show_main_menu(self):
        while True:
            print("\nWelcome to the Library Management System!")
            print("Main Menu:")
            print("1. Book Operations")
            print("2. User Operations")
            print("3. Author Operations")
            print("4. Quit")
            
            choice = input("Select an option: ")

            if choice == '1':
                self.book_operations()
            elif choice == '2':
                self.user_operations()
            elif choice == '3':
                self.author_operations()
            elif choice == '4':
                print("Quitting the application.")
                break
            else:
                print("Invalid option. Please try again.")

    def book_operations(self):
        while True:
            print("\nBook Operations:")
            print("1. Add a new book")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Search for a book")
            print("5. Display all books")
            print("6. Back to Main Menu")

            choice = input("Select an option: ")

            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.borrow_book()
            elif choice == '3':
                self.return_book()
            elif choice == '4':
                self.search_book()
            elif choice == '5':
                self.display_books()
            elif choice == '6':
                break
            else:
                print("Invalid option. Please try again.")

    def user_operations(self):
        while True:
            print("\nUser Operations:")
            print("1. Add a new user")
            print("2. View user details")
            print("3. Display all users")
            print("4. Back to Main Menu")

            choice = input("Select an option: ")

            if choice == '1':
                self.add_user()
            elif choice == '2':
                self.view_user_details()
            elif choice == '3':
                self.display_users()
            elif choice == '4':
                break
            else:
                print("Invalid option. Please try again.")

    def author_operations(self):
        while True:
            print("\nAuthor Operations:")
            print("1. Add a new author")
            print("2. View author details")
            print("3. Display all authors")
            print("4. Back to Main Menu")

            choice = input("Select an option: ")

            if choice == '1':
                self.add_author()
            elif choice == '2':
                self.view_author_details()
            elif choice == '3':
                self.display_authors()
            elif choice == '4':
                break
            else:
                print("Invalid option. Please try again.")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        genre = input("Enter genre: ")
        publication_date = input("Enter publication date: ")
        book = Book(title, author, genre, publication_date)
        self.books.append(book)
        print(f"Book '{title}' added successfully.")

    def borrow_book(self):
        title = input("Enter the title of the book to borrow: ")
        book = next((b for b in self.books if b.get_details()['Title'] == title), None)
        if book and book.borrow():
            user_id = input("Enter your library ID: ")
            user = next((u for u in self.users if u.get_details()['Library ID'] == user_id), None)
            if user and user.borrow_book(book):
                print(f"You have borrowed '{title}'.")
            else:
                book.return_book()  # Rollback
                print("Failed to borrow the book.")
        else:
            print("Book is not available or not found.")

    def return_book(self):
        title = input("Enter the title of the book to return: ")
        book = next((b for b in self.books if b.get_details()['Title'] == title), None)
        if book:
            user_id = input("Enter your library ID: ")
            user = next((u for u in self.users if u.get_details()['Library ID'] == user_id), None)
            if user and user.return_book(book):
                print(f"You have returned '{title}'.")
            else:
                print("Failed to return the book.")
        else:
            print("Book not found.")

    def search_book(self):
        title = input("Enter the title of the book to search for: ")
        book = next((b for b in self.books if b.get_details()['Title'] == title), None)
        if book:
            print(book.get_details())
        else:
            print("Book not found.")

    def display_books(self):
        if self.books:
            for book in self.books:
                print(book)
        else:
            print("No books available.")

    def add_user(self):
        name = input("Enter user name: ")
        library_id = input("Enter library ID: ")
        user = User(name, library_id)
        self.users.append(user)
        print(f"User '{name}' added successfully.")

    def view_user_details(self):
        library_id = input("Enter library ID to view details: ")
        user = next((u for u in self.users if u.get_details()['Library ID'] == library_id), None)
        if user:
            print(user.get_details())
        else:
            print("User not found.")

    def display_users(self):
        if self.users:
            for user in self.users:
                print(user)
        else:
            print("No users available.")

    def add_author(self):
        name = input("Enter author name: ")
        biography = input("Enter author biography: ")
        author = Author(name, biography)
        self.authors.append(author)
        print(f"Author '{name}' added successfully.")

    def view_author_details(self):
        name = input("Enter author name to view details: ")
        author = next((a for a in self.authors if a.get_details()['Name'] == name), None)
        if author:
            print(author.get_details())
        else:
            print("Author not found.")

    def display_authors(self):
        if self.authors:
            for author in self.authors:
                print(author)
        else:
            print("No authors available.")