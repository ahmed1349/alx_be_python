class Book:
    """Base class representing a book with a title and author."""

    def __init__(self, title, author):
        """Initialize the book with a title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a string representation of the book."""
        return f"'{self.title}' by {self.author}"


class EBook(Book):
    """Derived class representing an e-book with a file size."""

    def __init__(self, title, author, file_size):
        """Initialize the e-book with title, author, and file size."""
        super().__init__(title, author)
        self.file_size = file_size  # File size in MB

    def __str__(self):
        """Return a string representation of the e-book, including file size."""
        return f"{super().__str__()} (EBook, {self.file_size}MB)"


class PrintBook(Book):
    """Derived class representing a print book with a page count."""

    def __init__(self, title, author, page_count):
        """Initialize the print book with title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count  # Page count for print books

    def __str__(self):
        """Return a string representation of the print book, including page count."""
        return f"{super().__str__()} (PrintBook, {self.page_count} pages)"


class Library:
    """A Library class to manage a collection of books using composition."""

    def __init__(self):
        """Initialize the library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a book (Book, EBook, or PrintBook) to the library."""
        self.books.append(book)
    def list_books(self):
        """List all books in the library with their details."""
        if not self.books:
            print("The library has no books.")
            return
        for book in self.books:
            print(book)
