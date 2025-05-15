num1 = 1
num2 = 2
sum1 = num1 + num2

# print()會顯示參數值並換行
print(num1)
print(num2)

# 列印完不想換行，使用end指定要取代換行的字串
print(num1, num2, end=", ")
print(sum1)

# 列印多個參數可使用sep (separator) 指定分隔符號，
# 沒有使用end參數則列印完後仍舊會換行
print(num1, num2, sep=", ")
print(sum1)

# 既指定分隔符號，也指定列印完的結果
print(num1, num2, sep=" + ", end=" = ")
print(sum1)
