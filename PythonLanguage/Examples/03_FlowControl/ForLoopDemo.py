# 初始值為1，終止值為11(到11就停止，所以不會print 11），變化量為遞增1
for i in range(1, 11, 1):
    print(i, end=" ")
print()

# 初始值為1，終止值為11，變化量預設為遞增1
for i in range(1, 11):
    print(i, end=" ")
print()

# 初始值預設為0，終止值為11，變化量預設為遞增1
for i in range(11):
    print(i, end=" ")
print()

# 初始值為10，終止值為0（到0就停止，所以不會print 0），變化量為遞減1
for i in range(10, 0, -1):
    print(i, end=" ")
print()

# for-else
for i in range(1, 11):
    print(i, end=" ")
else:
    print("到11就停止")

