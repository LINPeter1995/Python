from myPackage.packageA.book import Book


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
