import json

# list
names = ["Python", "Java", "JS", "Swift", "C#"]

# dictionary
book = {
    "name": "Python",
    "price": 500,
    "author": "Paul"
}

# dictionaries inside a list
books = [
    {
        "name": "Python",
        "price": 500,
        "author": "Paul"
    },
    {
        "name": "Java",
        "price": 550,
        "author": "John"
    }
]


# 自訂類別
class Book:
    def __init__(self, name, price, author):
        self.name = name
        self.price = price
        self.author = author


def main():
    print("list轉JSON字串:")
    namesJsonStr = json.dumps(names)
    print(f"namesJsonStr type: {type(namesJsonStr)}\nnamesJsonStr: {namesJsonStr}")
    print()
    print("JSON字串轉list:")
    nameList = json.loads(namesJsonStr)
    print(f"nameList type: {type(nameList)}\nnameList: {nameList}")
    print("-----------------------------------")

    print("dictionary轉JSON字串:")
    bookJsonStr = json.dumps(book)
    print(f"bookJsonStr type: {type(bookJsonStr)}\nbookJsonStr: {bookJsonStr}")
    print()
    print("JSON字串轉dictionary:")
    bookDic = json.loads(bookJsonStr)
    print(f"bookDic type: {type(bookDic)}\nbookDic: {bookDic}")
    print("-----------------------------------")

    print("list(含有多個dictionary)轉JSON字串:")
    booksJsonStr = json.dumps(books)
    print(f"type: {type(booksJsonStr)}\nbooksJsonStr: {booksJsonStr}")
    print()
    print("JSON字串轉list(含有多個dictionary)")
    bookList = json.loads(booksJsonStr)
    print(f"bookList type: {type(bookList)}\nbookList: {bookList}")
    print("-----------------------------------")

    print("自訂物件先轉dictionary再轉JSON字串:")
    bookJsonStr = json.dumps(Book("Python", 500, "Paul").__dict__)
    print(f"type: {type(bookJsonStr)}\nbookJsonStr: {bookJsonStr}")
    print()
    print("JSON字串轉dictionary:")
    bookDic = json.loads(bookJsonStr)
    print(f"bookDic type: {type(bookDic)}\nbookDic: {bookDic}")


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
