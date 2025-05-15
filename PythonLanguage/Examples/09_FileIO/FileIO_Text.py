import locale
from pathlib import Path


def demoRead(filePath):
    # "r"(read)代表讀資料，"t"(text)代表文字內容；預設為"rt"，如果讀取文字檔案可省略不寫
    # f - file object
    # with區塊結束會自動關閉file，所以不需要呼叫f.close()
    # encoding(文字編碼)不區別大小寫，如果不設定，會採用該平台的encoding
    with filePath.open(mode="rt", encoding="UTF-8") as f:
        for line in f:
            print(line, end="")

        print("\n相關資訊: ")
        print(f"f.name: {f.name}")
        print(f"f.closed(with內): {f.closed}")
        print(f"f.mode: {f.mode}")
        print(f"f.encoding: {f.encoding}")
        print(f"system encoding: {locale.getpreferredencoding()}")

    print(f"f.closed(with外): {f.closed}")


def demoWrite(filePath):
    text = "春暖花開"
    # "w" (write) 代表寫入資料，如果寫入文字檔案可省略 "t" (text)
    with filePath.open(mode="w", encoding="UTF-8") as f:
        f.write(text)
    print("儲存完畢!")


def demoAppend(filePath):
    text = "秋高氣爽"
    # "a" (append) 代表在已有的檔案內容附加文字
    with filePath.open(mode="a", encoding="UTF-8") as f:
        f.write(text)
    print("附加完畢!")


def main():
    readDir = Path("09_FileIO", "read")
    writeDir = Path("09_FileIO", "write")
    # 存放目錄不存在就建立，相對路徑代表存放位置跟執行的Python檔案放在同一目錄
    writeDir.mkdir(exist_ok=True)

    print("demoRead():")
    # 建立欲讀取檔案的path物件
    readFile = readDir/"books.txt"
    demoRead(readFile)
    print("-----------------------------------")

    print("demoWrite():")
    # 建立欲寫入檔案的path物件
    writeFile = writeDir/"fileOut.txt"
    demoWrite(writeFile)
    print("-----------------------------------")

    print("demoAppend():")
    # 建立欲附加檔案的path物件
    appendFile = writeDir/"fileAppend.txt"
    demoAppend(appendFile)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
