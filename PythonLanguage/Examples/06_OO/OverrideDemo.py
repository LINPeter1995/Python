class Book:
    def __init__(self, name="", price=0.0, author=""):
        self.name = name
        self.price = price
        self.author = author

    def show(self):
        print(f"name: {self.name}")
        print(f"price: {self.price}")
        print(f"author: {self.author}")


# ComputerBook繼承Book
class ComputerBook(Book):
    # 子類別增加exampleUrl變數
    def __init__(self, name="", price=0.0, author="", exampleUrl=""):
        # 呼叫父類別__init__()
        super().__init__(name, price, author)
        self.exampleUrl = exampleUrl

    # override
    def show(self):
        super().show()
        print(f"examples URL: {self.exampleUrl}")


def main():
    python = ComputerBook("Python", 500, "Paul", "www.examples.com")
    python.show()


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
