from functools import reduce


class Book:
    def __init__(self, name="", price=0.0, author=""):
        self.name = name
        self.price = price
        self.author = author

    def show(self):
        print(f"name: {self.name}")
        print(f"price: {self.price}")
        print(f"author: {self.author}")


def obj_to_dict():
    print("Object to dictionary")
    book = Book("Python", 500, "Paul")
    print(f"book.__dict__:\n{book.__dict__}")
    print("-----------------------------------")
    print(f"vars(book):\n{vars(book)}")


def dict_to_obj():
    print("Dictionary to object")
    dictionary = {'name': 'Python', 'price': 500, 'author': 'Paul'}
    # The **dictionary syntax unpacks each dictionary and
    # passes its key-value pairs as keyword arguments to the Book constructor.
    book = Book(**dictionary)
    book.show()


def objs_to_dicts():
    print("Objects to dictionaries")
    books = [
        Book("Python", 500, "Paul"),
        Book("C++", 400, "Cindy"),
    ]

    dictionaries = [vars(book) for book in books]
    print(dictionaries)


def dicts_to_objs():
    print("Dictionaries to objects")
    dictionaries = [
        {'name': 'Python', 'price': 500, 'author': 'Paul'},
        {'name': 'C++', 'price': 400, 'author': 'Cindy'}
    ]

    books = [Book(**dictionary) for dictionary in dictionaries]
    for book in books:
        book.show()


def main():
    obj_to_dict()
    print("===================================")
    dict_to_obj()
    print("===================================")
    objs_to_dicts()
    print("===================================")
    dicts_to_objs()


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
