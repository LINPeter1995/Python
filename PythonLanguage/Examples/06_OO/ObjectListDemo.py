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


def main():
    myBooks = [
        Book("Python", 500, "Paul"),
        Book("C++", 400, "Cindy"),
        Book("MongoDB", 600, "Mike")
    ]

    print("map()將書名映射出來:")
    mapList = list(map(lambda book: book.name, myBooks))
    print(mapList)
    print("-----------------------------------")

    print("filter()列出含有mongo的書名，而且不區別大小寫:")
    filterList = list(
        filter(
            lambda book: "mongo".upper() in book.name.upper(),
            myBooks)
    )
    for b in filterList:
        b.show()
    print("-----------------------------------")

    print("max()列出最貴的書:")
    maxBook = max(myBooks, key=lambda book: book.price)
    maxBook.show()
    print("-----------------------------------")

    print("min()列出最便宜的書:")
    minBook = min(myBooks, key=lambda book: book.price)
    minBook.show()
    print("-----------------------------------")

    print("reduce()算出書價總和:")
    sum1 = reduce(lambda sum2, book: sum2 + book.price, myBooks, 0)
    print(sum1)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
