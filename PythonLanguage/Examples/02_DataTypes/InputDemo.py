name = input("請輸入姓名: ")
print(f"Hi, {name}")

# strip()可去除頭尾空白
name = input("請輸入姓名(會去除頭尾空白): ").strip()
print(f"Hi, {name}")

# int()會自動去除頭尾空白，所以無需再呼叫strip()
num1 = int(input("請輸入第一個整數: "))
num2 = int(input("請輸入第二個整數: "))
print(f"{num1} + {num2} = {num1 + num2}")

# 使用eval()會自動轉為適當類型，例如浮點數
num1 = eval(input("請輸入第一個小數: "))
num2 = eval(input("請輸入第二個小數: "))
print(f"{num1} + {num2} = {num1 + num2}")

# eval()不要直接用於非數字格式的文字，會產生NameError
yourName = eval(input("Your name: "))
print(f"Hi, {yourName}")