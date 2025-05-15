class ComputerBook:
    def __init__(self, exampleUrl=""):
        self.exampleUrl = exampleUrl

    def showExampleUrl(self):
        print("Computer Book")
        print(f"examples URL: {self.exampleUrl}")


class ComicBook:
    def __init__(self, poster=""):
        self.poster = poster

    def showPoster(self):
        print("Comic Book")
        print(f"poster: {self.poster}")


def main():
    cart = []
    computerBook = ComputerBook("www.examples.com")
    comicBook = ComicBook("Comic posters")
    cart.append(computerBook)
    cart.append(comicBook)
    for book in cart:
        # 檢查book是否屬於ComputerBook
        if isinstance(book, ComputerBook):
            book.showExampleUrl()
        elif isinstance(book, ComicBook):
            book.showPoster()


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
