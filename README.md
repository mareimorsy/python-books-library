# File based books application using python

## Requirements
* Python3.6 or later
* Available diskspace :joy:

## How to run 
```
python3.6 main.py
```

# Components
* `bookHandler.py` : it handles all books CRUD operations also you can think of this module as an ORM in modrn frameworks, so you can use it as following:
```
book = Book.findById(4) # Get the book which has the ID #4
book.title = "New title"
book.description = "New description"
book.update()
```

* `fileHandler.py` : it handles all the DB files I/O operations, there are several ways to manage file manipulation, like saving each row as a single line, seperated by a comma as columns, also updating specific bytes of the file, but I decided to keep it as simple as possible so I saved the whole file as a collection of JSON objects and recreating the file with every single change, the best part is that we can change the function implementation anytime and it won't affect the other parts of the code.

* `main.py` : it's the interface that handles the business logic of books console application.

# Enhancements/Todo
* Adding more validations
* Adding unit tests
* when updating a book we may update only that part of the file, also we could append to the file on creating new book instead of recreating the whole document
* also we could run all CRUD operations in-memory and only save it with the finall commit when we exit the application
* We could also save the books in order, so we could find it much faster using binary search algorithm
* Search optimizations and support searching by any field, also we could implement a very simple Full Text Search algorithm