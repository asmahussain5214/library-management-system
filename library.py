from database import load_books, save_books

def add_book():
    books = load_books()

    book_id = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "available": True
    }

    books.append(book)
    save_books(books)

    print("Book added successfully!")

def view_books():
    books = load_books()

    if not books:
        print("No books found")
        return

    for book in books:
        print(book)

def borrow_book():
    books = load_books()

    book_id = input("Enter Book ID to borrow: ")

    for book in books:
        if book["id"] == book_id and book["available"]:
            book["available"] = False
            save_books(books)
            print("Book borrowed successfully")
            return

    print("Book not available")

def return_book():
    books = load_books()

    book_id = input("Enter Book ID to return: ")

    for book in books:
        if book["id"] == book_id:
            book["available"] = True
            save_books(books)
            print("Book returned successfully")
            return

    print("Book not found")