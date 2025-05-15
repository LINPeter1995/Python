from pathlib import Path
from bs4 import BeautifulSoup


def selectAttribute(soup):
    # 搜尋id值為"myid1"的標籤
    print(f"soup.select('#myid1'):\n{soup.select('#myid1')}")
    # 等同於
    # print(f"soup(id='myid1'):\n{soup(id='myid1')}")
    print("-----------------------------------")
    # 搜尋id值為"myid1"或"myid2"
    print("soup.select('#myid1, #myid2'):")
    print(soup.select('#myid1, #myid2'))
    # 等同於
    # print(f"soup(id=['myid1', 'myid2']):\n{soup(id=['myid1', 'myid2'])}")
    print("-----------------------------------")
    # 搜尋class值為"frog"與"link1"(兩者都需要有)
    print(f"soup.select('a.frog.link1'):\n{soup.select('a.frog.link1')}")
    # 等同於
    # print("soup('a', class_='frog link1')")
    # print(soup('a', class_='frog link1'))
    print("-----------------------------------")
    # 搜尋所有<p>標籤，而且class值為"title"
    print(f"soup.select('p.title'):\n{soup.select('p.title')}")
    # 等同於
    # print(f"soup('p', class_='title'):\n{soup('p', class_='title')}")
    print("-----------------------------------")
    # 搜尋<p>直屬子標籤內的class值為"link1"。find_all()沒有對應寫法
    print(f"soup.select('p > .link1'):\n{soup.select('p > .link1')}")
    print("-----------------------------------")
    # 搜尋<p>直屬子標籤內的id值為"myid1"。find_all()沒有對應寫法
    print(f"soup.select('p > #myid1'):\n{soup.select('p > #myid1')}")
    print("-----------------------------------")
    # 搜尋<p>子標籤內的id值為"myid1"。沒有">"則非直屬子標籤內含有該id也可以
    print(f"soup.select('body > #myid1'):\n{soup.select('body > #myid1')}")
    print(f"soup.select('body #myid1'):\n{soup.select('body #myid1')}")
    print("-----------------------------------")
    # 搜尋所有符合屬性名稱為"name"與值為"comment"的標籤
    print("soup.select('[name='comment']'):")
    print(soup.select('[name="comment"]'))
    # 等同於
    # print("soup(attrs={'name': 'comment'}):")
    # print(soup(attrs={'name': 'comment'}))
    print("-----------------------------------")
    # 搜尋所有<a>標籤，但限縮在前2筆
    print(f"soup.select('a')[:2]:\n{soup.select('a')[:2]}")
    # 等同於
    # print(f"soup('a', limit=2):\n{soup('a', limit=2)}")


def main():
    path = Path("BeautifulSoup", "Index.html")
    with open(path, "r", encoding="UTF-8") as f:
        # 建立BeautifulSoup物件並指定檔案輸入物件
        soup = BeautifulSoup(f, "html.parser")

    selectAttribute(soup)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
