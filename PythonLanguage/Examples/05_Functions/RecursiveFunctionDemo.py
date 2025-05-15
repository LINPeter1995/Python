def recursive(count):
    if count > 0:
        print(count, end=" ")
        recursive(count - 1)


def loop(count):
    for number in range(count, 0, -1):
        print(number, end=" ")


def main():
    count = 10
    print("遞迴函式")
    recursive(count)
    print("\n--------------------------------------------")

    print("迴圈")
    loop(count)
    print()


# 可以確保該程式在被直接執行時會執行main()；被其他程式匯入時則不會執行main()
if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
