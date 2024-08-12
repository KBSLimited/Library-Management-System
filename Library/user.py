# library/user.py

class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.__borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.__borrowed_books:
            book.return_book()
            self.__borrowed_books.remove(book)
            return True
        return False

    def get_details(self):
        return {
            'Name': self.__name,
            'Library ID': self.__library_id,
            'Borrowed Books': [book.get_details()['Title'] for book in self.__borrowed_books]
        }

    def __str__(self):
        return f"User: {self.__name}, ID: {self.__library_id}"
