print("無參數、無回傳值")
def sayHello():
    print("Hello")

sayHello()
print("--------------------------------------------")

print("2個參數，無回傳值")
def showInfo(name, price):
    print(f"書名: {name}\n定價: {price}")

showInfo("Python", 500)
print("--------------------------------------------")

print("參數有預設值（default arguments）")
def showBookInfo(name, price, discount=0.2):
    info = f"書名: {name}\n售價: {price * (1 - discount)}"
    print(info)

# 呼叫時不傳值代表使用預設值
showBookInfo("Python", 500)
# 呼叫時也可傳值代表不使用預設值
showBookInfo("Python", 500, 0.3)
print("--------------------------------------------")

# 一個參數有預設值，其後的參數也必須有預設值，
# 否則產生 "non-default parameter follows default parameter" 錯誤
# def showBookInfo2(name, price=500, discount):
#     info = f"書名: {name}\n售價: {price * (1 - discount)}"
#     print(info)

print("2個參數與1個回傳值")
# 可以不定義回傳類型
def getInfo(name, price):
    info = f"書名: {name}\n定價: {price}"
    return info

result = getInfo("Python", 500)
print(result)
print("--------------------------------------------")

print("也可定義回傳類型")
def getInfo2(name, price) -> str:
    info = f"書名: {name}\n定價: {price}"
    return info

result = getInfo2("Python", 500)
print(result)
print("--------------------------------------------")

print("多個參數與多個回傳值 (其實是回傳tuple)")
def getSaleInfo(name, price, discount):
    salePrice = price * (1 - discount)
    info = f"書名: {name}\n定價: {price}"
    return salePrice, info
# 使用索引取值
result = getSaleInfo("Python", 500, 0.2)
print(f"{result[1]}\n特價: {result[0]}")
# 使用變數取值
salePrice, info = getSaleInfo("Python", 500, 0.2)
print(f"info:\n{info}\nsalePrice: {salePrice}")
print("--------------------------------------------")

print("*args(Arbitrary Positional Arguments)")
# 一個函式只能定義一個*args，否則錯誤
def addNumbers(*numbers):
    print(f"{numbers}，總和{sum(numbers)}")

addNumbers(1, 2, 3, 4)
print("--------------------------------------------")

print("**kwargs: Arbitrary Keyword Arguments")
# 一個函式只能定義一個**kwargs，否則錯誤
def showEmployee(**employee):
    for key, value in employee.items():
        print(f"{key}: {value}")

showEmployee(name="John", age=30, city="Taipei")
print("--------------------------------------------")

print("同時使用*args與**kwargs")
def args_kwargs(*args, **kwargs):
    print(f"args: {args}\nkwargs: {kwargs}")

args_kwargs(1, 2, 3, 4, name="John", age=30, city="Taipei")
print("--------------------------------------------")

print("keyword arguments")
# 不指定名稱，需按照參數順序；指定名稱，可以不按照順序
def showBook(name, price, discount):
    info = f"書名: {name}\n售價: {price * (1 - discount)}"
    print(info)

showBook("Python", discount=0.2, price=500)
print("--------------------------------------------")
