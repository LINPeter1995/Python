# 建立好dictionary，但未存放元素
# bookDic = {}
# 建立並同時存放3組資料
bookDic = {
    "name": "Python",
    "price": 500,
    "author": "Paul"
}
print(f"bookDic: {bookDic}")
# 取得dictionary長度
print(f"len(bookDic): {len(bookDic)}")

# 透過key取value，若無該key會產生KeyError
name = bookDic["name"]
# 也可呼叫get()取值
# name = bookDic.get("name")
print(f"name: {name}")

# 取得keys
print("keys:", end=" ")
for key in bookDic.keys():
    print(key, end=" ")
print()

# 取得values
print("values:", end=" ")
for value in bookDic.values():
    print(value, end=" ")
print()

# 使用items()取得keys與values
print("items:")
for key, value in bookDic.items():
    print(f"{key} - {value}")

# 檢查key是否存在
key = "price"
if key in bookDic:
    print(f"{key}這個key已存在")

# 改變指定key的value
bookDic["author"] = "Peter"
print(f"author值改為'Peter': {bookDic}")

# 新增key-value
bookDic["isbn"] = "123456789012"
print(f"新增isbn資料: {bookDic}")

# 移除指定key代表的資料，若沒有該key，產生KeyError
bookDic.pop("isbn")
print(f"移除isbn資料: {bookDic}")

# 複製dictionary
bookDicCopy = bookDic.copy()
print(f"複製dictionary: {bookDicCopy}")

# 清空dictionary內容
bookDic.clear()
print(f"清空dictionary內容: {bookDic}")
