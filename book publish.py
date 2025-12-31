class Publisher:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Publisher: ", self.name)

class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)
        self.title = title
        self.author = author

    def display(self):
        super().display()
        print("Title: ", self.title)
        print("Author: ", self.author)

class Python(Book):
    def __init__(self, name, title, author, price, pages):
        super().__init__(name, title, author)
        self.price = price
        self.pages = pages

    def display(self):
        super().display()
        print("Price: ", self.price)
        print("Pages: ", self.pages)

pub = input("Enter Publisher name: ")
title = input("Enter Title: ")
author = input("Enter Author name: ")
price = int(input("Enter price: "))
pages = int(input("Enter pages: "))

p = Python(pub, title, author, price, pages)

print("\n====Book Details====")
p.display()