class Book:
    def __init__(self, name="", price=0.0, author=""):
        # self.name, self.price, self.author會宣告物件的屬性(實例變數)
        self.name = name
        self.price = price
        self.author = author

    def show(self):
        print(f"name: {self.name}")
        print(f"price: {self.price}")
        print(f"author: {self.author}")

    # 同一個類別不能宣告相同名稱方法，因為Python不支援method overloading
    # 但可由預設值設定達到method overloading功能
    def salePrice(self, discount=0.0):
        return self.price * (1 - discount)


def main():
    book1 = Book()
    book1.name = "Python"
    book1.price = 500
    book1.author = "Paul"
    book1.show()
    print(f"售價(沒折扣): {book1.salePrice()}")
    print("-----------------------------------")
    book2 = Book("C++", 400, "Cindy")
    book2.show()
    print(f"售價(打八折): {book2.salePrice(0.2)}")


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
