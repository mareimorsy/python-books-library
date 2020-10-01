from bookHandler import *

def main():
    while True:
        menu_options = input("""==== Book Manager ====

        1) View all books
        2) Add a book
        3) Edit a book
        4) Search for a book
        5) Save and exit

        \b\b\b\b\b\b\b\bChoose [1-5]: """)

        if(menu_options == '1'):
            view_all_books()
        elif(menu_options == '2'):
            add_book()
        elif(menu_options == '3'):
            edit_book()
        elif(menu_options == '4'):
            search_book()
        elif(menu_options == '5'):
            print("\nLibrary saved.")
            break
        else:
            print("\nInvalid Option\n")

def search_book():
    print("==== Search for a book ====\n\nType in one or more keywords to search for\n")
    search = input("Search: ")
    results = Book.search(search)
    if(len(results)):
        for book in results:
            print("[{}] {}".format(book['id'], book['title']))
            while True:
                print("\nTo view details enter the book ID, to return press <Enter>.\n")
                bookID = input("Book ID: ")
                if (bookID == ""):
                    break
                else:
                    book = Book.findById(int(bookID))
                    if (book is None):
                        print("\nCan't find a book with ID #{}\n".format(bookID))
                    else:
                        print("ID: {}\nTitle: {}\nAuthor: {}\nDescription:{}".format(book.id, book.title, book.author, book.description))
    else:
        print("\nCan't find search results about {}\n".format(search))



def edit_book():
    print("==== Edit a book ====\n")
    books = Book.all()
    for book in books:
        print("[{}] {}".format(book['id'], book['title']))
    while True:
        print("\nEnter the book ID of the book you want to edit; to return press <Enter>.\n")
        bookID = input("Book ID: ")
        if (bookID == ""):
            break
        else:
            book = Book.findById(int(bookID))
            if (book is None):
                print("Can't find a book with ID #{}".format(bookID))
            else:
                print("\nInput the following information. To leave a field unchanged, hit <Enter>\n")
                book.title = input("Title: ")
                book.author = input("Author: ")
                book.description = input("Description: ")
                book.update()
                print("\nBook Saved\n")


def add_book():
    print("==== Add a book ====\n")
    # Auto generate new ID
    books = Book.all()
    if(len(books)):
        generated_id = books[-1]['id'] + 1
    else:
        generated_id = 1
    title = input("Title: ")
    author = input("Author: ")
    description = input("Description: ")
    Book(generated_id, title, author, description).save()
    print("\nBook [{}] Saved\n".format(generated_id))
    


    

def view_all_books():
    print("==== View Books ====\n")
    books = Book.all()
    for book in books:
        print("[{}] {}".format(book['id'], book['title']))
    while True:
        print("\nTo view details enter the book ID, to return press <Enter>.\n")
        bookID = input("Book ID: ")
        if (bookID == ""):
            break
        else:
            book = Book.findById(int(bookID))
            if (book is None):
                print("Can't find a book with ID #{}".format(bookID))
            else:
                print("ID: {}\nTitle: {}\nAuthor: {}\nDescription:{}".format(book.id, book.title, book.author, book.description))


    

if __name__ == '__main__':
    main()