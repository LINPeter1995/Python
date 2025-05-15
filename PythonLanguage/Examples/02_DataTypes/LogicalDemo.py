# Logical - AND
money = 30000
day = 7
travel = money >= 100000 and day >= 10
if travel:
    print("可以去澳洲看黃金海岸")
else:
    print("只能在公園看黃金獵犬")

# Logical - OR
aircraft = True
boat = True
result = aircraft or boat
print(f"是否成行: {result}")

# Logical - NOT
age = 16
adult = age >= 18
if not adult:
    print(f"{age} 歲不可進入觀賞")
