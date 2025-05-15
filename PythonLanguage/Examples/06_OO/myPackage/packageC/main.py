from myPackage.packageA.book import Book
from myPackage.packageB.computer import ComputerBook


def main():
    book = Book("Gone with the Wind", 550, "Mitchell, Margaret")
    book.show()
    print("----------------------------------------")
    pythonBook = ComputerBook("Python", 500, "Paul", "www.examples.com")
    pythonBook.show()


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
