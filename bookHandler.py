from fileHandler import *
import json
class Book:
    def __init__(self, id, title, author, description):
        self.id = id
        self.title = title
        self.author = author
        self.description = description

    @staticmethod
    def all():
        return json.loads(readFile("books.json"))

    @staticmethod
    def findById(id):
        books = Book.all()
        for book in books:
            if (book['id'] == id):
                return Book(book['id'], book['title'], book['author'], book['description']) 

    @staticmethod
    def search(title):
        books = Book.all()
        result = []
        for book in books:
            if (title.lower() in book['title'].lower()):
                result.append(book)
        return result

    @staticmethod
    def delete(id):
        books = Book.all()
        new_books = []
        for book in books:
            if (book['id'] != id):
                new_books.append(book)
        writeFile("books.json", json.dumps(new_books))

    def update(self):
        books = Book.all()
        print(self.__dict__)
        new_books = []
        for book in books:
            if (book['id'] == self.id):
                new_books.append(self.__dict__)
            else:
                new_books.append(book)
        writeFile("books.json", json.dumps(new_books))

    def save(self):
        books = Book.all()
        books.append(self.__dict__)
        writeFile("books.json", json.dumps(books))