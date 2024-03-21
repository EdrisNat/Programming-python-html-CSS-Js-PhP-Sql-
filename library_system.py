class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def get_info(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nGenre: {self.genre}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("No books in the library yet.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(book.get_info())
                print("-" * 20)


# Demonstration
# Create some book instances
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction")
book3 = Book("1984", "George Orwell", "Dystopian Fiction")

# Create a library instance
library = Library()

# Add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Display the books in the library
library.display_books()
