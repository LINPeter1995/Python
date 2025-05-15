class Book:
    """提供書相關功能的類別"""
    # name, price, author為變數，又稱為屬性，屬於物件所有
    # name = ""
    # price = 0.0
    # author = ""
    # __init__參數如有包含對應屬性名稱，則屬性定義可以省略

    def __init__(self, name="", price=0.0, author=""):
        """
        name: 書名
        price: 定價
        author: 作者
        """
        self.name = name
        self.price = price
        self.author = author

    def show(self):
        """ 顯示一本書的資訊 """
        print(f"name: {self.name}")
        print(f"price: {self.price}")
        print(f"author: {self.author}")

    # 同一個類別不能宣告相同名稱方法， 因為Python不支援method overloading
    # 但可由預設值設定達到method overloading功能
    def salePrice(self, discount=0.0):
        """回傳折扣後的售價"""
        return self.price * (1 - discount)


def main():
    book2 = Book("C++", 400, "Cindy")
    book2.show()
    print(f"售價(打八折): {book2.salePrice(0.2)}")
    print("-----------------------------------")

    print("列印類別的docstrings:")
    print(Book.__doc__)
    print("-----------------------------------")
    print("列印建構函式的docstrings:")
    print(Book.__init__.__doc__)
    print("-----------------------------------")
    print("列印函式的docstrings:")
    print(Book.salePrice.__doc__)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")

