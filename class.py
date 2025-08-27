class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def read(self):
        print(f"Reading '{self.title}' by {self.author} 📖 - class.py:7")
class Novel(Book):
    def read(self): 
        print(f"Enjoying the story of '{self.title}' ❤️ - class.py:10")

class Textbook(Book):
    def read(self):
        print(f"Studying knowledge from '{self.title}' 📚 - class.py:14")

class Comic(Book):
    def read(self):
        print(f"Laughing at fun scenes in '{self.title}' 😂 - class.py:18")

library = [
    Novel("Pride and Prejudice", "Jane Austen"),
    Textbook("Physics 101", "Dr. Newton"),
    Comic("Spider-Man", "Stan Lee")
]

for book in library:
    book.read()
