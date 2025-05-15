def divide(dividend, divisor):
    quotient = dividend / divisor
    print(f"{dividend} / {divisor} = {quotient}")


def main():
    try:
        dividend = int(input("請輸入被除數: "))
        divisor = int(input("請輸入除數: "))
        divide(dividend, divisor)
    # except有繼承關係，則子型要排在前，父型要在後；沒有繼承關係，可以自由排列
    except ValueError as err:
        print(f"ValueError: {err}")
    except ZeroDivisionError:
        print("ZeroDivisionError: 除數不可為0")
    # 若ZeroDivisionError與ArithmeticError順序顛倒會有警示訊息: Code is unreachable
    except ArithmeticError as err:
        print(f"ArithmeticError: {err}")
    else:
        print("else: 除法運算結束")
    finally:
        print("finally: 釋放佔用的資源")


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
