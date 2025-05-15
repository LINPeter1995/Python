from pathlib import Path
import re
from bs4 import BeautifulSoup


def selectRegex(soup):
    # 精準比對，所以找不到id為"myid"的標籤
    print(f"soup.select('#myid'): {soup.select('#myid')}")
    print("-----------------------------------")
    # 搜尋所有id含有"myid"的標籤
    print("soup.select('[id*='myid']')")
    print(soup.select("[id*='myid']"))
    # 等同於
    # print(f"soup(id=re.compile('myid')):\n{soup(id=re.compile('myid'))}")
    print("-----------------------------------")
    # 搜尋所有class開頭有"tit"的標籤
    print("soup.select('[class^='tit']'):")
    print(soup.select("[class^='tit']"))
    # 等同於
    # print(f"soup(class_=re.compile('^tit')):\n{soup(class_=re.compile('^tit'))}")
    print("-----------------------------------")
    # 搜尋所有href結尾有"frog2"標籤
    print("soup.select('[href$='frog2']')")
    print(soup.select("[href$='frog2']"))
    # 等同於
    # print(f"soup(href=re.compile('frog2$')):\n{soup(href=re.compile('frog2$'))}")
    print("-----------------------------------")
    # 設定多個條件：搜尋所有<a>而且href含有"frog"而且id為"myid1"的標籤
    print(f"soup.select('a[href*='frog'][id='myid1']'):")
    print(soup.select("a[href*='frog'][id='myid1']"))
    # 等同於
    # print(f"soup('a', href=re.compile('frog'), id='myid1'):")
    # print(soup('a', href=re.compile('frog'), id='myid1'))


def main():
    path = Path("BeautifulSoup", "Index.html")
    with open(path, "r", encoding="UTF-8") as f:
        # 建立BeautifulSoup物件並指定檔案輸入物件
        soup = BeautifulSoup(f, "html.parser")

    selectRegex(soup)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
