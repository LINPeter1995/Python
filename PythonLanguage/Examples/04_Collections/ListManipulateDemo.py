names = ["Python", "Java", "JS", "Swift", "C#"]

# 設定值
names[0] = "Python 3"
print(f"改變索引0的值: {names}")

# 附加值
names.append("Ruby")
print(f"附加Ruby: {names}")

# 插入值到指定索引
names.insert(5, "Go")
print(f"插入Go到索引5位置: {names}")

# 移除指定值，若無該值，產生ValueError
names.remove("Go")
print(f"移除Go: {names}")
# 可先確定有值，然後再移除，以避免ValueError
if "Go" in names:
    names.remove("Go")
    print(f"移除Go: {names}")
else:
    print(f"找不到'Go'值，無法移除")

# 移除指定索引的值，若list為空或索引超過界線，產生IndexError
print(f"移除索引5的值: {names.pop(5)}")
print(f"names: {names}")

# 移除末端值，若list為空，產生IndexError
print(f"移除末端值: {names.pop()}")
print(f"names: {names}")

# 複製一個新的 list，並非參照
namesCopy = names.copy()
namesCopy.pop()
print(f"namesCopy: {namesCopy}")

# 合併2個list
others = ["Go", "Ruby"]
listJoin = names + others
print(f"合併2個list: {listJoin}")

# 清空list內容
names.clear()
print(f"清空list內容: {names}")







