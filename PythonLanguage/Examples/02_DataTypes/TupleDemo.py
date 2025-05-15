# tuple儲存多個值，透過index取值
bookNames = ("Python", "MySQL", "JavaScript", "Python")
print(f"bookNames[0]: {bookNames[0]}")
# index(value)搜尋指定元素所在位置
print(f"bookNames.index('Python'): {bookNames.index('Python')}")
# count(value)計算指定元素出現幾次
print(f"bookNames.count('Python'): {bookNames.count('Python')}")
# len(tuple)回傳元素個數
print(f"len(bookNames): {len(bookNames)}")
# 取出所有元素值
text = "所有書名："
for name in bookNames:
    text += name + " "
print(text)

# tuple可以加、乘
books01 = ("Python", "Java", "JavaScript")
books02 = ("MySQL", "MongoDB")
print(f"books01 + books02: {books01 + books02}")
print(f"books01 * 2: {books01 * 2}")

# 元素類型可以不同
book = ("Python", 500, "Paul")
print(f"book1[1]: {book[1]}")

# Tuple不支援值指派，會執行失敗
# bookNames[2] = "Java"






