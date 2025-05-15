from pathlib import Path
import requests
from bs4 import BeautifulSoup


def htmlDoc():
    htmlDoc = """<!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>HTML文件</title>
    </head>
    <body>
        <h1>Hello World!</h1>
    </body>
    </html>"""
    # 可以讀HTML文字內容
    # 建立BeautifulSoup物件並指定HTML文字內容
    soup = BeautifulSoup(htmlDoc, "html.parser")
    print(f"HTML文字內容:\n{soup}")


def htmlFile(path):
    # 搭配open()可以讀HTML檔案內容
    # f - file object
    # with區塊結束會自動關閉file，所以不需要呼叫f.close()
    # 如果不設定encoding(文字編碼)，會採用該平台的encoding
    with open(path, "r", encoding="UTF-8") as f:
        # 建立BeautifulSoup物件並指定檔案輸入物件
        soup = BeautifulSoup(f, "html.parser")

    print(f"HTML檔案:\n{soup}")


def webPage():
    # 搭配requests可以讀遠端網頁內容
    # 取得指定網址的網頁內容
    response = requests.get("https://reqres.in/api/users/2")
    # 檢查request是否成功，如果成功status code為200
    if response.status_code == 200:
        # 建立BeautifulSoup物件並指定網頁內容
        soup = BeautifulSoup(response.text, "html.parser")
        print(f"遠端網頁:\n{soup}")
    else:
        print(f"請求失敗，status code: {response.status_code}")


def main():
    htmlDoc()
    print("===================================")
    path = Path("BeautifulSoup", "Index.html")
    htmlFile(path)
    print("===================================")
    webPage()


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
