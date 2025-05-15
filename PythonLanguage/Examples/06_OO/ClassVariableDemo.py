class Book:
    # 類別變數
    count = 0

    # 類別方法
    @classmethod
    def showCount(cls):
        print(f"count: {cls.count}")

    def __init__(self, name="", price=0.0, author=""):
        Book.count += 1
        # self.name, self.price, self.author會宣告實例變數
        self.name = name
        self.price = price
        self.author = author

    def show(self):
        print(f"name: {self.name}")
        print(f"price: {self.price}")
        print(f"author: {self.author}")


def main():
    Book.showCount()
    print("-----------------------------------")
    book1 = Book("Python", 500, "Paul")
    book1.show()
    print("-----------------------------------")
    book2 = Book("C++", 400, "Cindy")
    book2.show()
    print("-----------------------------------")
    Book.showCount()


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
