import requests
from bs4 import BeautifulSoup

def main():
    url = "https://www.tenlong.com.tw/search?availability=buyable&display=list&keyword=python&langs%5B%5D=all"
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}
    # 網站起始url
    urlStart = "https://www.tenlong.com.tw"

    number = int(input("要顯示幾頁? "))
    for i in range(number):
        print(url)
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"請求失敗，status code: {response.status_code}")
            return
        soup = BeautifulSoup(response.text, "html.parser")
        # 取得網頁內容
        content = getPageContent(soup)
        print(content)
        # 取得下頁連結
        a = soup.select_one("a.next_page")
        url = urlStart + a["href"]


# 取得網頁內容
def getPageContent(soup):
    content = ""
    # <div class="book-data">內有書的資訊
    for div in soup.select("div.book-data"):
        # 取得書名
        name = div.a.text.strip()
        # 取得出版日期
        publishDate = div.select_one("span.publish-date").text.strip()
        # 取得定價
        price = div.select_one("span.price").text.strip()
        content += f"{price}\t{publishDate}\t{name}\n"

    return content

main()
