from pathlib import Path
import re
from bs4 import BeautifulSoup


def findAllRegex(soup):
    # 沒有使用正規表示式，就是精準比對，所以找不到id為"id"的標籤
    print(f"soup(id='myid'): {soup(id='myid')}")
    print("-----------------------------------")
    # 使用正規表示式代表搜尋所有id含有"myid"的標籤
    print(f"soup(id=re.compile('myid')):\n{soup(id=re.compile('myid'))}")
    print("-----------------------------------")
    # 搜尋所有class開頭有"link"的標籤
    print(
        f"soup(class_=re.compile('^link')):\n{soup(class_=re.compile('^link'))}")
    print("-----------------------------------")
    # 搜尋所有href結尾有"frog2"標籤
    print(
        f"soup(href=re.compile('frog2$')):\n{soup(href=re.compile('frog2$'))}")
    print("-----------------------------------")
    # 設定多個條件：搜尋所有<a>而且href含有"frog"而且id為"myid1"的標籤
    print(f"soup('a', href=re.compile('frog'), id='myid1'):")
    print(soup('a', href=re.compile('frog'), id='myid1'))
    print("-----------------------------------")


def findAllStr(soup):
    # 搜尋指定文字值。回傳的是文字值，並非標籤
    print(f"soup(string='井底之蛙的故事')):\n{soup(string='井底之蛙的故事')}")
    print("-----------------------------------")
    # 搜尋符合list內任一文字值
    print(f"soup(string=['小青', '小蛙']):\n{soup(string=['小青', '小蛙'])}")
    # 搜尋符合list內任一文字值，搭配正規表示式
    print(f"soup(string=[re.compile('青'), re.compile('蛙')]):")
    print(soup(string=[re.compile('青'), re.compile('蛙')]))
    print("-----------------------------------")
    # 搜尋所有<a>含有"蛙"文字值
    print(
        f"soup('a', string=re.compile('蛙')):\n{soup('a', string=re.compile('蛙'))}")


def main():
    path = Path("BeautifulSoup", "Index.html")
    with open(path, "r", encoding="UTF-8") as f:
        # 建立BeautifulSoup物件並指定檔案輸入物件
        soup = BeautifulSoup(f, "html.parser")

    findAllRegex(soup)
    findAllStr(soup)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
