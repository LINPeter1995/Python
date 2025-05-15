#請輸入被除數: 10 
#請輸入除數: 3 
#10 // 3 = 3 ... 1    
# 從用戶那裡獲取被除數和除數
dividend = int(input("請輸入被除數: "))
divisor = int(input("請輸入除數: "))

# 計算整數除法和餘數
result = dividend // divisor  # 整數除法
remainder = dividend % divisor  # 餘數

# 顯示結果
print(f"{dividend} // {divisor} = {result} ... {remainder}")

