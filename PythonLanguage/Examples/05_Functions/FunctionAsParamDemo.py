# op_func是函式型參數
def showDivide(op_func, num1, num2):
    quotient = op_func(num1, num2)
    print(f"{num1} / {num2} = {quotient}")


# 常見的函式型參數應用：別人寫好的功能函式，例如按鈕點擊事件處理
def button_click(button, task):
    print(f"偵測到使用者點擊 {button} 按鈕...")
    # 呼叫傳入的欲執行的內容
    task()


def main():
    def divide(dividend, divisor):
        quotient = dividend / divisor
        return quotient

    showDivide(divide, 10, 2)
    print("------------------------------------")

    # 當使用者點擊新增按鈕時，新增一筆資料
    def insert():
        print("新增一筆資料...")
        print("新增成功!")

    button_click("新增", insert)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
