class Book:
    def __init__(self, name="", price=0.0, author=""):
        self.name = name
        self.price = price
        self.author = author


def main():
    book1 = Book("Python", 500, "Paul")
    book2 = Book("JS", 500, "John")
    print(f"id(book1): {id(book1)}\nid(book2): {id(book2)}")
    print(f"book1 == book2: {book1 == book2}")
    print(f"book1 is book2: {book1 is book2}")
    print("-----------------------------------")

    book1 = book2
    print("執行 book1 = book2 以後: ")
    print(f"id(book1): {id(book1)}\nid(book2): {id(book2)}")
    print(f"book1 == book2: {book1 == book2}")
    print(f"book1 is book2: {book1 is book2}")


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
