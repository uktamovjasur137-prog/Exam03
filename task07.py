class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

book1 = Book("harry potter", "rowling", 1990)
book2 = Book("O/'tkan kunlar", "abdulla qodiriy", 1900)

print(book1.title, book1.author, book1.year)
print(book2.title, book2.author, book2.year)
