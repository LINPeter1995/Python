import random

names = ["Python", "Java", "JS", "Swift", "C#"]
name = "Python"

# 回傳搜尋到元素的索引，搜尋不到產生ValueError
firstIndex = names.index(name)
print(f"{name}所在索引: {firstIndex}")

# 反向排序，會改變原先元素排列方式
names.reverse()
print(f"反向排序: {names}")

# 升冪排序
names.sort()
print(f"升冪排序: {names}")

# 降冪排序
names.sort(reverse=True)
print(f"降冪排序: {names}")

# 隨機重排
random.shuffle(names)
print(f"隨機重排: {names}")
