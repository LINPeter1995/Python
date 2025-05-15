# 相同package可以省略package名稱
from myPackage.packageA.product import Product


class Book(Product):
    def __init__(self, name="", price=0.0, author=""):
        super().__init__(name, price)
        self.author = author

    def show(self):
        print(f"name: {self.name}")
        print(f"price: {self.price}")
        print(f"author: {self.author}")