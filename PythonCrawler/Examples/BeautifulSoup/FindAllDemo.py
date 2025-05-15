from pathlib import Path
import re
from bs4 import BeautifulSoup


def findAll(soup):
    # 搜尋所有<a>標籤並列出內容
    print(f"soup.find_all('a'):\n{soup.find_all('a')}")
    # 也可改用「soup.("標籤名")」
    print(f"soup('a'):\n{soup('a')}")
    print("-----------------------------------")
    # 搜尋所有<a>標籤，並將href屬性值列出
    print("list(map(lambda a: a['href'], soup('a'))):")
    print(list(map(lambda a: a['href'], soup('a'))))


def main():
    path = Path("BeautifulSoup", "Index.html")
    with open(path, "r", encoding="UTF-8") as f:
        # 建立BeautifulSoup物件並指定檔案輸入物件
        soup = BeautifulSoup(f, "html.parser")

    findAll(soup)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
