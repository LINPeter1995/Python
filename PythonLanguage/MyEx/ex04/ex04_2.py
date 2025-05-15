#請問有幾個好友? 5 
#請輸入第1個好友名與⾝上現⾦: Mary 2000 
#請輸入第2個好友名與⾝上現⾦: John 1000 
#請輸入第3個好友名與⾝上現⾦: Sue 800 
#請輸入第4個好友名與⾝上現⾦: Linda 1200 
#請輸入第5個好友名與⾝上現⾦: Ken 500 -------------------------------------------------- 
#請輸入欲借現⾦: 1200 
#可借錢的好友: Mary, Linda, 共2⼈
goodFirends = {
    "Mary":2000,
    "John":1000,
    "Sue":800,
    "Linda":1200,
    "Ken":500
}
print(f"goodFirends: {goodFirends}")
print(f"請問有幾個好友? {len(goodFirends)}個")

# 取得⾝上現⾦
print(f"⾝上現⾦:")
for value in goodFirends.values():
    print(value, end=" ")
print()

# 使用items()取得keys與values
print("可借錢的好友:")
for key, value in goodFirends.items():
    if value >= 1200:
        print(f"{key}: {value}元")
    
