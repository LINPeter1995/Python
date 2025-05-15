

class Book:
    def __init__(self, price=0.0):
        self.price = price


# 傳值
def pass_by_value(number):
    number2 = number
    number2 *= 0.8
    print(f"number2 = {number2}")


# 傳參照
def pass_by_reference(book):
    book2 = book
    book2.price *= 0.8
    print(f"book2.price = {book2.price}")


def main():
    print("傳值: ")
    number1 = 500
    print(f"number1 = {number1}")
    pass_by_value(number1)
    print(f"number1 = {number1}")
    print("-----------------------------------")

    print("傳參照: ")
    book1 = Book()
    book1.price = 500.0
    print(f"book1.price = {book1.price}")
    pass_by_reference(book1)
    print(f"book1.price = {book1.price}")


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
