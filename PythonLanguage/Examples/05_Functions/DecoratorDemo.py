def myDecorator(func):
    def wrapper():
        print("Before function is called.")
        func()
        print("After function is called.")

    return wrapper


# 使用decorator目的就是在不影響原來函式情況下，加上其他功能，兼具重複利用與模組化
# 刪除「@myDecorator」就等於只呼叫sayHello()，而不會先呼叫myDecorator(func)
@myDecorator
def sayHello():
    print("Hello!")


def beef(func):
    def wrapper(text):
        result = func(text)
        return f"牛肉 {result}"

    return wrapper


# 可以再定義一個pork(func)，然後在meal(text)上加「@pork」
def pork(func):
    def wrapper(text):
        result = func(text)
        return f"豚骨 {result}"

    return wrapper


# 刪除「@beef」就等於只呼叫meal(text)，而不會先呼叫beef(func)
@beef
# @pork
def meal(text):
    return text


def main():
    # 呼叫sayHello()時會先呼叫myDecorator(func)並將sayHello函式名稱傳給func，然後得到wrapper
    # 所以呼叫sayHello()等於呼叫wrapper()
    sayHello()
    print("------------------------------------")

    # 呼叫meal()時會先呼叫beef(func)並將meal函式名稱傳給func，然後得到wrapper
    # 所以呼叫meal("拉麵")等於呼叫wrapper("拉麵")
    print(meal("拉麵"))


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
