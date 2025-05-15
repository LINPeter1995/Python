class Book:

    def __init__(self, name, price, author):
        # self.name屬於public
        self.name = name
        # 宣告private屬性並給予初始值。不能直接將接到的引數值指派給"__price"，這樣不會執行setter檢查
        self.__price = 0
        # 這樣才會執行setter
        self.price = price
        # protected屬性
        self._author = author

    # 因為 __price為private，要讓類別以外地區可以存取必須建立 getter / setter
    # getter
    @property
    def price(self):
        # 是self.__price，而非self.price(會一直遞迴呼叫此函式)
        return self.__price

    # setter檢查傳入值是否正確，正確才將值指派給屬性
    @price.setter
    def price(self, price):
        if price < 0:
            print(f"價格不可以為{price}，維持原值!")
        else:
            self.__price = price


class ComputerBook(Book):
    pass


def main():
    computerBook = ComputerBook("Python", -500, "Paul")
    print(computerBook.name)
    print(computerBook.price)
    # private屬性不能被外部存取
    # print(computerBook.__price)
    # 子型可以存取protected屬性，但仍建議使用getter
    print(computerBook._author)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
