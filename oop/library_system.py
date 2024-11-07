class Book:
    """Base class representing a book with a title and author."""

    def __init__(self, title, author):
        """Initialize the book with a title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a string representation of the book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an e-book with a file size in KB."""

    def __init__(self, title, author, file_size_kb):
        """Initialize the e-book with title, author, and file size in KB."""
        super().__init__(title, author)
        self.file_size_kb = file_size_kb  # File size in KB

    def __str__(self):
        """Return a string representation of the e-book, including file size in KB."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size_kb}KB"


class PrintBook(Book):
    """Derived class representing a print book with a page count."""

    def __init__(self, title, author, page_count):
        """Initialize the print book with title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count  # Page count for print books

    def __str__(self):
        """Return a string representation of the print book, including page count."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


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