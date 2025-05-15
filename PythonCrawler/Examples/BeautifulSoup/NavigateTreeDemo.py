from pathlib import Path
from bs4 import BeautifulSoup


def main():
    path = Path("BeautifulSoup", "Index.html")
    with open(path, "r", encoding="UTF-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    # 取得上一層父標籤
    print(f"soup.title.parent.name:\n{soup.title.parent.name}")
    print("-----------------------------------")
    # 取得所有父標籤
    print("for parent in soup.title.parents:")
    for parent in soup.title.parents:
        print(parent.name)
    print("-----------------------------------")
    tag = soup.find(string="小青").find_parent()
    print(f"取得內含'小青'文字的標籤:\n{tag}")
    print("-----------------------------------")
    print(f"soup.p:\n{soup.p}")
    # 取得指定子標籤
    print(f"soup.p.b:\n{soup.p.b}")
    print("-----------------------------------")
    # 取得所有子元件
    print("for child in soup.p.children:")
    for child in soup.p.children:
        print(child)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
