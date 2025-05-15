print("文字串接")
s1 = "Hello " + "World!"
print(s1)

a = 35
b = 20
# 將數字轉成文字後方能串接
s2 = "a = " + str(a) + ", b = " + str(b) + "; a x b = " + str(a * b)
print(s2)

# Python 3.6 開始支援 f-strings
s3 = f"a = {a}, b = {b}; a x b = {a * b}"
print(s3)
print("===================================")

print("格式化")
# 數字格式化符號參看：
# https://docs.python.org/3.6/library/string.html#format-specification-mini-language

num1 = 10000.0
num2 = 3.0

## 格式化數字
# 使用 f-strings
print(f"{num1:.2f} / {num2:.2f} = {num1 / num2:,.2f}")
print("-----------------------------------")

# 使用str.format()
# "0:"代表指定index為0的值，也就是num1
print("{0} / {1} = {2}".format(num1, num2, num1 / num2))
# ".2f"代表留2位小數，第3位四捨五入；","代表千分位符號
print("{0:.2f} / {1:.2f} = {2:,.2f}".format(num1, num2, num1 / num2))
# 建議省略index，會依序指定index為0, 1, 2...的值
print("{:.2f} / {:.2f} = {:,.2f}".format(num1, num2, num1 / num2))
print("===================================")

print("進階格式化")
# 使用 f-strings
# "<"代表對齊左邊；">"代表對齊右邊；"10"代表會補齊10個字元
print(f"{'Name':<10}{'BMI':>7}{'Weight':>8}")
# 預設文字對齊左邊，數字對齊右邊；"7.1f"代表總位數7位，小數位數1位
print(f"{'John':10}{24.123:7.1f}{72.355:8.1f}")
print(f"{'Allen':10}{40.673:7.1f}{106.345:8.1f}")
print(f"{'Sue':10}{19.543:7.1f}{45.235:8.1f}")
print("-----------------------------------")

# 使用str.format()
print("{0:<10}{1:>7}{2:>8}".format("Name", "BMI", "Weight"))
print("{0:10}{1:7.1f}{2:8.1f}".format("John", 24.123, 72.355))
print("{0:10}{1:7.1f}{2:8.1f}".format("Allen", 40.673, 106.345))
print("{0:10}{1:7.1f}{2:8.1f}".format("Sue", 19.543, 45.235))




