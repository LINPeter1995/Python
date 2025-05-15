# 自訂執行錯誤類別
class BookError(BaseException):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"BookError: {self.message}"


class Book:
    def __init__(self, name, price, author):
        self.name = name
        self.__price = 0.0
        self.price = price
        self.author = author

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        # 當價格不正確，產生BookError
        if price < 0.0:
            raise BookError(f"價格不正確: {price}")
        else:
            self.__price = price

    def __str__(self):
        return f"name: {self.name}, price: {self.price}, author: {self.author}"


def main():
    try:
        book = Book("Python", -500, "Paul")
        print(book)
    except BookError as err:
        print(err)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
