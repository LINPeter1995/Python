class Book:
    def __init__(self, name="", price=0.0, author=""):
        self.name = name
        self.price = price
        self.author = author

    def show(self):
        print(f"name: {self.name}")
        print(f"price: {self.price}")
        print(f"author: {self.author}")


class ComputerBook(Book):
    def __init__(self, name="", price=0.0, author="", exampleUrl=""):
        super().__init__(name, price, author)
        self.exampleUrl = exampleUrl

    def show(self):
        super().show()
        self.showExampleUrl()

    def showExampleUrl(self):
        print(f"examples URL: {self.exampleUrl}")


class ComicBook(Book):
    def __init__(self, name="", price=0.0, author="", poster=""):
        super().__init__(name, price, author)
        self.poster = poster

    def show(self):
        super().show()
        self.showPoster()

    def showPoster(self):
        print(f"poster: {self.poster}")


def main():
    cart = []
    python = ComputerBook("Python", 500, "Paul", "www.examples.com")
    onePiece = ComicBook("One Piece", 120, "Oda Eiichiro", "One Piece posters")
    cart.append(python)
    cart.append(onePiece)
    print("購物車資訊如下：")
    for book in cart:
        print("-----------------------------------")
        book.show()


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
