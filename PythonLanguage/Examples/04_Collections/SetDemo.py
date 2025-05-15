# 建立好set，但未存放元素
# names = set()
# 不可使用此方式建立set，會被誤以為dictionary
# names = {}
# 建立並同時存放文字元素
names = {"Python", "Java", "JS", "Swift", "C#"}

# 取得set長度
print(f"len(names): {len(names)}")

# 取出所有元素
print(f"for迴圈取出所有元素:", end=" ")
for name in names:
    print(name, end=" ")
print()

# 檢查set是否存在指定值，沒有則新增
name = "Python"
if name in names:
    print(f"{name}在其內")
else:
    names.add(name)

# 欲加入的元素如果與Set內既存的元素值相同，則無法加入
names.add("Go")
print(f"新增Go: {names}")

# 使用discard()移除元素，即使沒有該元素也不會產生KeyError；remove()則否
names.discard("Go")
# names.remove("Go")
print(f"移除元素Go: {names}")

# 複製set
namesCopy = names.copy()
print(f"複製set: {namesCopy}")

# set轉成list
myList = list(names)
print(f"set轉成list: {myList}")

# list轉成set (list元素值如有重複會被去除)
mySet = set(myList)
print(f"list轉成set: {mySet}")

# 清空set內容
names.clear()
print(f"清空set內容: {names}")

# set集合運算
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
c = {1, 2}
d = {1, 2}
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")
print(f"d: {d}")
print(f"a.intersection(b): {a.intersection(b)}")
print(f"a.union(b): {a.union(b)}")
print(f"a.symmetric_difference(b): {a.symmetric_difference(b)}")
print(f"c.issubset(a): {c.issubset(a)}")
print(f"c.issubset(d): {c.issubset(d)}")
print(f"a.issuperset(c): {a.issuperset(c)}")
print(f"b.isdisjoint(c): {b.isdisjoint(c)}")
print(f"c == d: {c == d}")
print(f"c is d: {c is d}")









