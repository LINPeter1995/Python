from operator import attrgetter


class Book:
    def __init__(self, isbn, name="", price=0.0):
        self.isbn = isbn
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.isbn == other.isbn

    # def __hash__(self):
    #     return hash(self.isbn)

    def show(self):
        print(f"ISBN: {self.isbn}, name: {self.name}, price: {self.price}")

    @staticmethod
    def showAll(books):
        for book in books:
            book.show()


def main():
    myBooks = [
        Book("123456", "Python", 500),
        Book("789012", "C++", 400),
        Book("345678", "JS", 500)
    ]
    # 搜尋自訂物件需要覆寫 __eq__()，而無須覆寫 __hash__()
    print("搜尋物件，回傳所在索引: ")
    jsBook = Book("345678", "JS", 500)
    print(f"index: {myBooks.index(jsBook)}")
    print("-----------------------------------")

    # 排序功能可套用在List與Set
    # 可以使用lambda指定要比對的屬性，預設為升冪，reverse=True則為降冪
    print("價格升冪排序:")
    Book.showAll(sorted(myBooks, key=lambda book: book.price))
    print("-----------------------------------")

    print("價格降冪排序:")
    Book.showAll(sorted(myBooks, key=lambda book: book.price, reverse=True))
    print("-----------------------------------")

    # 也可以引用operator的attrgetter()指定要比對的屬性
    print("價格升冪後書名升冪排序:")
    Book.showAll(sorted(myBooks, key=attrgetter("price", "name")))


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
