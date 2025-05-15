from pathlib import Path
import re
from bs4 import BeautifulSoup


# 定義下列過濾用的函式
# 搜尋有class屬性但沒有id屬性的標籤
def has_class_but_no_id(tag):
    return tag.has_attr("class") and not tag.has_attr('id')


# 搜尋href不含有'frog3'的標籤
def no_frog3_link(href):
    return href and not re.compile("frog3").search(href)


def main():
    path = Path("BeautifulSoup", "Index.html")
    with open(path, "r", encoding="UTF-8") as f:
        # 建立BeautifulSoup物件並指定檔案輸入物件
        soup = BeautifulSoup(f, "html.parser")

    print("搜尋有class屬性但沒有id屬性的標籤:")
    print(soup(has_class_but_no_id))
    print("-----------------------------------")

    print("回傳href不含有'frog3'的標籤:")
    # 會將soup內所有href值傳給函式
    print(soup(href=no_frog3_link))


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
