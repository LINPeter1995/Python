from bs4 import BeautifulSoup

with open("basic.html", "r", encoding="UTF-8") as fp:
    soup = BeautifulSoup(fp, "html.parser")

# 先將程式結果print出來觀察是否正確
# print(soup.ul("li"))
# 取得<ul>內所有<li>的文字
for tag in soup.ul("li"):
    text = tag.text
    print(text)

# 先將程式結果print出來觀察是否正確
# print(soup("a", string="GOOGLE搜尋網站"))
# 取得"GOOGLE搜尋網站"的超連結
for a in soup("a", string="GOOGLE搜尋網站"):
    print(a["href"])
