def divide(dividend, divisor):
    quotient = dividend / divisor
    return quotient


def main():
    # divide函式指派給op_func
    op_func = divide
    result = op_func(10, 2)
    print(f"op_func(10, 2): {result}")


# 可以確保該程式在被直接執行時會執行main()；被其他程式匯入時則不會執行main()
if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
