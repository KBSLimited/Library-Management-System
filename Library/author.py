# library/author.py

class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    def get_details(self):
        return {
            'Name': self.__name,
            'Biography': self.__biography
        }

    def __str__(self):
        return self.__name
