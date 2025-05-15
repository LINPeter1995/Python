from bs4 import BeautifulSoup


def main():
    with open("table.html", "r", encoding="UTF-8") as fp:
        soup = BeautifulSoup(fp, "html.parser")
        method01(soup)
        method02(soup)

# 檢查不是標題列的資料才儲存
def method01(soup):
    friends = []
    # print(soup.select("table tr"))
    trs = soup.select("table tr")
    for tr in trs:
        # print(tr.select_one("th"))
        if tr.select_one("th") is None:
            friend = []
            for td in tr.select("td"):
                friend.append(td.text)
            friends.append(friend)
    print(friends)

# 跳過第一列(標題列)
def method02(soup):
    friends = []
    # print(soup.select("table tr"))
    trs = soup.select("table tr")
    # 第一個<tr>的index為0，儲存的是標題不是資料內容，所以從index為1開始取值
    for i in range(1, len(trs)):
        tr = trs[i]
        friend = []
        for td in tr.select("td"):
            friend.append(td.text)
        friends.append(friend)
    print(friends)


main()
