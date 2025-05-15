from pathlib import Path
import re
from bs4 import BeautifulSoup


# 搭配BeautifulSoup提供的關鍵字：id, class_, href, attrs
# 因為"class"為Python關鍵字，所以BeautifulSoup改為"class_"
def findAllAttribute(soup):
    # 搜尋id值為"myid1"的標籤
    print(f"soup(id='myid1'):\n{soup(id='myid1')}")
    print("-----------------------------------")
    # 搜尋id值為"myid1"或"myid2"
    print(f"soup(id=['myid1', 'myid2'])\n{soup(id=['myid1', 'myid2'])}")
    print("-----------------------------------")
    # 搜尋class值為"frog"與"link1"(兩者都需要有)
    print("soup('a', class_='frog link1')")
    print(soup('a', class_='frog link1'))
    print("-----------------------------------")
    # 搜尋id有值的所有標籤
    print(f"soup(id=True):")
    for tag in soup(id=True):
        print(f"{tag.name}: id={tag['id']}")
    print("-----------------------------------")
    # 搜尋所有<p>標籤，而且class值為"title"；
    print(f"soup('p', class_='title'):\n{soup('p', class_='title')}")
    # 或改成下列寫法，第二個值"title"代表的也是class
    print(f"soup('p', 'title'):\n{soup('p', 'title')}")
    print("-----------------------------------")
    # BeautifulSoup沒有提供name關鍵字來指定HTML的name屬性，所以要改用attrs來指定
    # 搜尋所有符合屬性名稱為"name"與值為"comment"的標籤
    print("soup(attrs={'name': 'comment'}):")
    print(soup(attrs={'name': 'comment'}))
    print("-----------------------------------")
    # limit參數: 搜尋所有<a>標籤，但限縮在前2筆
    print(f"soup('a', limit=2):\n{soup('a', limit=2)}")


def main():
    path = Path("BeautifulSoup", "Index.html")
    with open(path, "r", encoding="UTF-8") as f:
        # 建立BeautifulSoup物件並指定檔案輸入物件
        soup = BeautifulSoup(f, "html.parser")

    findAllAttribute(soup)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
