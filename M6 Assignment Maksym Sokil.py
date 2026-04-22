class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self._isbn = isbn
        self._checked_out = False

    @property
    def isbn(self):
        return self._isbn

    @property
    def checked_out(self):
        return self._checked_out

    def borrow(self):
        if self._checked_out:
            return False
        self._checked_out = True
        return True

    def return_book(self):
        if not self._checked_out:
            return False
        self._checked_out = False
        return True

    def __str__(self):
        status = "Checked Out" if self._checked_out else "Available"
        return f"Book: {self.title} by {self.author} | ISBN: {self._isbn} | Status: {status}"


class EBook(Book):
    def __init__(self, title, author, isbn, file_size_mb):
        super().__init__(title, author, isbn)
        self.file_size_mb = file_size_mb

    def borrow(self):
        if self.checked_out:
            return False
        self._checked_out = True
        return True

    def __str__(self):
        status = "Checked Out" if self.checked_out else "Available"
        return (
            f"EBook: {self.title} by {self.author} | ISBN: {self.isbn} | "
            f"File Size: {self.file_size_mb} MB | Status: {status}"
        )


class Patron:
    def __init__(self, name, email):
        self.name = name
        self._email = email
        self.borrowed_books = []

    @property
    def email(self):
        return self._email

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name} successfully borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is already checked out.")

    def return_book(self, book):
        if book in self.borrowed_books and book.return_book():
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} cannot return '{book.title}'.")

    def show_books(self):
        if not self.borrowed_books:
            print(f"{self.name} has no borrowed books.")
        else:
            print(f"{self.name}'s borrowed books:")
            for book in self.borrowed_books:
                print(f" - {book.title}")

    def __str__(self):
        return f"Patron: {self.name} | Email: {self._email} | Borrowed Books: {len(self.borrowed_books)}"


def main():
    book1 = Book("1984", "George Orwell", "9780451524935")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")
    ebook1 = EBook("Python Crash Course", "Eric Matthes", "9781593279288", 12.5)

    patron1 = Patron("Maksym Sokil", "maksym@example.com")
    patron2 = Patron("Alex Carter", "alex@example.com")

    print("Initial Library Items:")
    print(book1)
    print(book2)
    print(ebook1)
    print()

    patron1.borrow_book(book1)
    patron1.borrow_book(ebook1)
    patron2.borrow_book(book1)
    print()

    patron1.show_books()
    patron2.show_books()
    print()

    print("Updated Library Items:")
    print(book1)
    print(book2)
    print(ebook1)
    print()

    patron1.return_book(book1)
    patron2.borrow_book(book1)
    print()

    patron1.show_books()
    patron2.show_books()
    print()

    print("Final Library Items:")
    print(book1)
    print(book2)
    print(ebook1)


if __name__ == "__main__":
    main()