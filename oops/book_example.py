class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __repr__(self):
        return f"Title = {self.title}, Pages = {self.pages}"

    # def __str__(self):
    #     return f"Title: {self.title}, Pages: {self.pages}"

    # this is instance method, which can be call from object
    def increase_pages(self, pages_increase):
        self.pages += pages_increase

    def decrease_pages(self, pages_decrease):
        self.pages -= pages_decrease


book1 = Book('My first book', 100)
book2 = Book('My second book', 200)

print(book1)
print(book2)

book1.increase_pages(50)
book2.decrease_pages(5)

print(book1)
print(book2)
