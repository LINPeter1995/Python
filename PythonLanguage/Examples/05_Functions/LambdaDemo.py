def maxNumber(num1, num2, max):
    print(f"maximum: {max(num1, num2)}")


def main():
    print("函式指派給參數")

    def maximum(num1, num2):
        return num1 if num1 > num2 else num2

    maxNumber(1, 2, maximum)
    print("-----------------------------------")

    print("lambda指派給參數")
    maxNumber(1, 2, lambda num1, num2: num1 if num1 > num2 else num2)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
