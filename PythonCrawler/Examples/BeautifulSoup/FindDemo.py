from pathlib import Path
from bs4 import BeautifulSoup


def main():
    path = Path("BeautifulSoup", "Index.html")
    with open(path, "r", encoding="UTF-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    # 「soup.find('標籤名')」找到第一個指定標籤即停止，並取得該標籤及其內容
    print(f"soup.find('title'):\n{soup.find('title')}")
    # 也可改用「soup.標籤名」
    print(f"soup.title:\n{soup.title}")
    print("-----------------------------------")
    # 如果標籤不存在會得到None，可用is檢查
    if soup.x is None:
        print("soup.x不存在")
    print("-----------------------------------")
    # 取得<title>標籤名稱
    print(f"soup.title.name:\n{soup.title.name}")
    print("-----------------------------------")
    # 取得<title>標籤文字值
    print(f"soup.title.text:\n{soup.title.text}")
    print(f"soup.title.string:\n{soup.title.string}")
    # text會取出該標籤內所有文字，包含子標籤
    print(f"soup.p.text:\n{soup.p.text}")
    # 如果標籤內有多個子元件，例如有文字值和子標籤，string會回傳None
    print(f"soup.p.string:\n{soup.p.string}")
    print("-----------------------------------")
    # 取得<p>標籤及其內容
    print(f"soup.p:\n{soup.p}")
    # 只取得<p>標籤的內容
    print(f"soup.p.contents:\n{soup.p.contents}")
    print("-----------------------------------")
    # 取得<a>標籤指定屬性的值
    print(f"soup.a['href']:\n{soup.a['href']}")
    print("-----------------------------------")
    # 如果標籤的屬性不存在，會產生KeyError，需使用try-except
    try:
        print(f"soup.a['x']:\n{soup.a['x']}")
    except KeyError:
        print("soup.a['x']不存在")
    print("-----------------------------------")
    # 也可呼叫get('attribute')取標籤內指定屬性的值
    print(f"soup.a.get('href'):\n{soup.a.get('href')}")
    print("-----------------------------------")
    # get('attribute')取屬性值時，如果該屬性不存在，會得到None，可用is檢查，較方便
    if soup.a.get('x') is None:
        print("soup.a.get('x')不存在")
    print("-----------------------------------")
    # 指定<a>標籤內的class屬性，其值可能有多個，所以回傳list
    print(f"soup.a['class']:\n{soup.a['class']}")
    print("-----------------------------------")
    # 可搭配索引取值
    print(f"soup.a['class'][0]:\n{soup.a['class'][0]}")
    print("-----------------------------------")
    # 取得<a>標籤內的所有屬性，回傳dictionary
    print(f"soup.a.attrs:\n{soup.a.attrs}")
    print("-----------------------------------")
    # 使用key指定欲取得的屬性值
    print(f"soup.a.attrs['class']:\n{soup.a.attrs['class']}")


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
