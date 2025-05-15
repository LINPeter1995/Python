def math(op):
    match op:
        case "+":
            return add
        case "-":
            return subtract
        case _:
            print(f"{op} 符號不正確，採用預設的加法運算")
            # 回傳函式
            return add


def add(num1, num2):
    return f"{num1} + {num2} = {num1 + num2}"


def subtract(num1, num2):
    return f"{num1} - {num2} = {num1 - num2}"


def main():
    op = input("請輸入運算符號: ")
    calculate = math(op)
    result = calculate(5, 3)
    print(result)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
