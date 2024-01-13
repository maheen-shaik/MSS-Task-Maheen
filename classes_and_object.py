class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def set_information(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def display_information(self):
        print("Title:",self.title)
        print("Author:",self.author)
        print("Genre:",self.genre)

# Create an instance of the Book class
my_book = Book(title="Five point Someone", author="Chetan Bhagat", genre="Fiction")
# Display initial information
print("Initial Information:")
my_book.display_information()
# Set new information using the set_information method
my_book.set_information(title="Mother I Never Knew", author="Sudha Murthy", genre="Fiction")
# Display updated information
print("\nUpdated Information:")
my_book.display_information()
