# 限制輸入次數，最多 10 次
for i in range(10):
    unlucky_number = input("不吉利數字 (1 ~ 9): ")
    
    # 檢查輸入是否是有效數字（1~9）
    if unlucky_number and 1 <= int(unlucky_number) <= 9:
        unlucky_number = int(unlucky_number)
        break  # 輸入有效，跳出迴圈
    else:
        print("輸入錯誤，請再輸入一次")

    # 檢查 1 到 49 的數字，排除包含不吉利數字的
    numbers = []
    for j in range(1, 50):
        if str(unlucky_number) not in str(j):  # 檢查數字的個位或十位數中是否有不吉利數字
            numbers.append(j)

    # 顯示剩下的數字，按每行 10 個數字顯示
    print("可選擇的數字：")
    for i in range(0, len(numbers), 10):
        print(" ".join(f"{num:02d}" for num in numbers[i:i+10]))

    # 顯示總個數
    print(f"總個數: {len(numbers)}")

