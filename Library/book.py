# library/book.py

class Book:
    def __init__(self, title, author, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__available = True

    def borrow(self):
        if self.__available:
            self.__available = False
            return True
        return False

    def return_book(self):
        self.__available = True

    def is_available(self):
        return self.__available

    def get_details(self):
        return {
            'Title': self.__title,
            'Author': self.__author,
            'Genre': self.__genre,
            'Publication Date': self.__publication_date,
            'Available': self.__available
        }

    def __str__(self):
        return f"'{self.__title}' by {self.__author}"
