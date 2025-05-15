from abc import abstractmethod, ABC, ABCMeta


# 可以透過「metaclass=ABCMeta」建立抽象類別
# class TestABC(metaclass=ABCMeta):
#     pass


# 也可以透過繼承ABC類別建立抽象類別；比較簡單，建議採用此種方式
class Sale(ABC):
    def __init__(self, discount=0.0):
        self.discount = discount

    # 抽象方法
    @abstractmethod
    def salePrice(self): pass

    # 抽象方法
    @abstractmethod
    def description(self): pass


class Book(Sale):
    def __init__(self, discount=0.0, name="", price=0, author=""):
        super().__init__(discount)
        self.name = name
        self.price = price
        self.author = author

    def salePrice(self):
        return self.price * (1 - self.discount)

    def description(self):
        return f"book name: {self.name}\n" \
            f"sale price: {self.salePrice()}\n" \
            f"author: {self.author}"


class Toy(Sale):
    def __init__(self, discount=0.0, name="", price=0, maker=""):
        super().__init__(discount)
        self.name = name
        self.price = price
        self.maker = maker

    def salePrice(self):
        return self.price * (1 - self.discount)

    def description(self):
        return f"toy name: {self.name}\n" \
            f"sale price: {self.salePrice()}\n" \
            f"marker: {self.maker}"


def main():
    cart = [Book(0.1, "Python", 500, "Paul"), Toy(
        0.3, "Hello Kitty", 200, "Kitty Inc.")]
    total = 0.0
    text = ""
    for item in cart:
        total += item.salePrice()
        text += item.description() + "\n----------------\n"

    text += f"total: {total}"
    print(text)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
