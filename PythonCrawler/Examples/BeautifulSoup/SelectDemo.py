from pathlib import Path
from bs4 import BeautifulSoup


def selectTag(soup):
    # select_one()搜尋到第一個符合的標籤就停止
    # 以下3種方式結果相同
    print(f"soup.select_one('a'):\n{soup.select_one('a')}")
    print(f"soup.a:\n{soup.a}")
    print(f"soup.select('a'):\n{soup.find('a')}")
    print("-----------------------------------")
    # select()會搜尋所有符合的標籤，以下3種方式結果相同
    print(f"soup.select('a'):\n{soup.select('a')}")
    print(f"soup('a'):\n{soup('a')}")
    print(f"soup.find_all('a'):\n{soup.find_all('a')}")
    print("-----------------------------------")

    # 搜尋<body>內的子標籤<a>，不是直屬標籤也在搜尋範圍內
    print(f"soup.select('body a'):\n{soup.select('body a')}")
    print("-----------------------------------")
    # 搜尋<body>內的直屬子標籤<a>，非直屬的<a>不在搜尋範圍內
    print(f"soup.select('body > a'): {soup.select('body > a')}")
    # 搜尋<p>的直屬子標籤<a>
    print(f"soup.select('p > a'):\n{soup.select('p > a')}")


def main():
    path = Path("BeautifulSoup", "Index.html")
    with open(path, "r", encoding="UTF-8") as f:
        # 建立BeautifulSoup物件並指定檔案輸入物件
        soup = BeautifulSoup(f, "html.parser")

    selectTag(soup)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
