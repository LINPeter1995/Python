i = 1
# type()用於檢查型別
print(f"type(i): {type(i)}")
d = 11.1
print(f"type(d): {type(d)}")

# 整數與浮點數運算會自動轉為浮點數
sum1 = i + d
print(f"sum1: {sum1}")

# int()用於轉成整數，float()用於轉成浮點數
sum2 = int(i + d)
print(f"sum2: {sum2}")

# str()用於轉成文字
numberStr = str(20)

# 文字轉數字
num1 = int("1")
num2 = float("11.1")
sum3 = num1 + num2
print(f"sum3: {sum3}")
# 文字轉數字有可能錯誤
# num3 = int("x123")

