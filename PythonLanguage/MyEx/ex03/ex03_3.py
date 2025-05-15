
# 計算總和
total = 0

# 使用 for 迴圈列印每一行的數字
for i in range(1, 41, 1):
    # 每10個數字換一行
    total += i
    if (i - 1) % 10 == 0:
        print()  # 換行
    print(f"{i:02d}", end=" ")  # 格式化為兩位數字，並在數字間加上空格

# 輸出總和
print("\n總和:", total)

