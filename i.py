# Created by: Jared Christopher
# File: i.py

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

class BookCatalog:
    def __init__(self):
        self.books = []

    def add_book_to_catalog(self, book):
        self.books.append(book)
        print(f"Added book '{book.title}' by {book.author} to catalog.")

    def remove_book_from_catalog(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Removed book '{book.title}' by {book.author} from catalog.")
        else:
            print("Book not found in catalog.")

    def generate_overdue_report(self):
        print("Generating overdue report for books.")

    def generate_popularity_report(self):
        print("Generating book popularity report.")

class BookSearch:
    def search_by_title(self, title):
        print(f"Searched for '{title}'.")

    def search_by_author(self, author):
        print(f"Searched for books by '{author}'.")

    def search_by_genre(self, genre):
        print(f"Searched for books in '{genre}' genre.")

class BookBorrowing:
    def borrow_book(self, book):
        print(f"Borrowing the book '{book.title}'.")

    def return_book(self, book):
        print(f"Returning the book '{book.title}'.")

    def generate_borrowing_report(self):
        print("Generating borrowing report.")

class Librarian(BookSearch, BookBorrowing, BookCatalog):
    pass

class User(BookSearch, BookBorrowing):
    pass

class Guest(BookSearch):
    pass

def main():
    librarian = Librarian()
    user = User()
    guest = Guest()

    print("\nLibrarian Actions:")
    book1 = Book("The Fellowship of the Ring", "J.R.R. Tolkien", "Fantasy")
    book2 = Book("The Two Towers", "J.R.R. Tolkien", "Fantasy")
    librarian.add_book_to_catalog(book1)
    librarian.add_book_to_catalog(book2)
    librarian.remove_book_from_catalog(book2)
    librarian.generate_overdue_report()
    librarian.borrow_book(book1)
    librarian.generate_popularity_report()
    librarian.return_book(book1)

    print("\nUser Actions:")   
    user.search_by_author("J.R.R. Tolkien")
    user.borrow_book(book1)
    user.return_book(book1)
    user.generate_borrowing_report()

    print("\nGuest Actions:")
    guest.search_by_genre("Fantasy")

if __name__ == "__main__":
    main()
