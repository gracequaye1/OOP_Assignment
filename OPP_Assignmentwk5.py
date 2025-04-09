# Superclass
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.__is_available = True  # Encapsulation: private attribute

    def read(self):
        return f"You're reading '{self.title}' by {self.author}."

    def borrow(self):
        if self.__is_available:
            self.__is_available = False
            return f"You've borrowed '{self.title}'."
        else:
            return f"'{self.title}' is already borrowed."

    def return_book(self):
        self.__is_available = True
        return f"'{self.title}' has been returned. Thank you!"

    def check_availability(self):
        return self.__is_available


# Subclass (Inheritance)
class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size  # In MB

    # Polymorphism: override read method
    def read(self):
        return f"You're reading the digital version of '{self.title}' ({self.file_size}MB) on your device."


# Create objects
physical_book = Book("The Act of Public Speacking", "God's_Girl_Grace", 200)
digital_book = EBook("Good Eating Habits", "James Addo", 300, 6)

# Test methods
print(physical_book.read())
print(physical_book.borrow())
print(physical_book.borrow())  # Try borrowing again
print(physical_book.return_book())

print(digital_book.read())
