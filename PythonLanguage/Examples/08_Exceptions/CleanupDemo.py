from pathlib import Path


def finallyClose(path):
    print("finallyClose():")
    f = None
    try:
        # open()可以開啟檔案，可能產生OSError
        # "r"(read)代表讀資料，"t"(text)代表文字內容；預設為"rt"，如果讀取文字檔案可省略不寫
        # f - file object
        f = open(path, "rt")
        for line in f:
            print(line, end="")
    except OSError as err:
        print(f"err: {err}")
    finally:
        # 無論是否發生exception，都需要f.close()，所以放在finally子句
        # 發生exception時，f會維持None，f.close()會產生錯誤，所以要檢查
        if f is not None:
            f.close()


def autoClose(path):
    print("autoClose():")
    try:
        # with區塊結束會自動關閉f，所以不需要呼叫f.close()
        with open(path, "rt") as f:
            for line in f:
                print(line, end="")
    except OSError as err:
        print(f"err: {err}")


def main():
    # 檔案路徑
    path = Path("08_Exceptions", "books.txt")

    finallyClose(path)
    print("-----------------------------------")
    autoClose(path)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
