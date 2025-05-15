# 建立好list，但未存放元素
# names = []
# 使用range()建立list所需的數字值
numbers = list(range(1, 10, 2))
print(f"numbers: {numbers}")

# 建立list並同時給予初始值
names = ["Python", "Java", "JS", "Swift", "C#"]
print(f"names: {names}")

# 取得list長度
print(f"len(names): {len(names)}")

# 取出索引為0的元素
print(f"names[0]: {names[0]}")

# 取後面數來第1個元素
print(f"names[-1]: {names[-1]}")

# 取索引0(含)到5(不含)的元素
print(f"names[0:5]: {names[0:5]}")
print(f"names[0:]: {names[0:]}")
print(f"names[:5]: {names[:5]}")
print(f"names[:]: {names[:]}")

# [start:stop:step]
print(f"names[0:5:2]: {names[0:5:2]}")

# 取後面數來第5個(含)到第1個(不含)元素
print(f"names[-5:-1]: {names[-5:-1]}")

# 取值順序必須左到右，右到左無法取出值
print(f"names[-1:-5]: {names[-1:-5]}")

# 索引超過界線會產生錯誤 IndexError: list index out of range
# print(f"names[5]: {names[5]}")

# 取出所有元素
print(f"for迴圈取出所有元素: ", end=" ")
for name in names:
    print(name, end=" ")
print()

# 截取使用者輸入的長寬高後，轉成數字並計算體積
cuboid = []
inputTexts = input("請輸入立方體長寬高: ").split()
for text in inputTexts:
    cuboid.append(int(text))

# 也可改成下列寫法
# 1. 類似for-in loop
# cuboid = [int(numberStr) for numberStr in input("請輸入立方體長寬高: ").split()]
# 2. 使用集合函式，第1個參數int為函式: int(number)，可將每個元素轉成整數
# cuboid = list(map(int, input("請輸入立方體長寬高: ").split()))

volume = 1
for number in cuboid:
    volume *= number
print(f"體積: {volume}")

