import re
import requests
from bs4 import BeautifulSoup


# 最新頁面網址
url = "https://www.ptt.cc/bbs/MobileComm/index.html"
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}
# 網站起始url
urlStart = "https://www.ptt.cc"


def previousPageUrl(soup):
    # 先使用Chrome觀察如何取得上頁連結
    links = soup.select("div.btn-group.btn-group-paging a")
    # 因為上頁連結排在第2個，所以index為1
    return links[1]["href"]


def bySelect(number):
    pageUrl = url
    for i in range(number):
        print(pageUrl)
        response = requests.get(pageUrl, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        # 取得網頁內容
        content = getPageContent(soup)
        print(content)
        pageUrl = urlStart + previousPageUrl(soup)


def byPageNumer(number):
    # 最新頁面
    print(url)
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"請求失敗，status code: {response.status_code}")
        return
    soup = BeautifulSoup(response.text, "html.parser")
    # 最新頁面內容
    content = getPageContent(soup)
    print(content)

    # 最新頁面為index.html，沒有頁碼，先取得上一頁連結並觀察頁碼
    previousUrl = previousPageUrl(soup)

    # 去除URL的分隔符號"/" (+ 代表1個以上) 後會得到list，最後一個元素為網頁檔名
    # 例如："/bbs/MobileComm/index7063.html" 會得到"index7063.html"
    pageName = re.compile(r"/+").split(previousUrl)[-1]
    # print(f"pageName: {pageName}")

    # 尋找網頁檔名中含有的數字，也就是頁碼
    # 例如："index7063.html"會得到"7063"
    numbers = re.findall(r"[0-9]+", pageName)
    # 檢查是否有頁碼
    if numbers:
        pageNumber = int(numbers[0])
        # print(f"pageNumber: {pageNumber}")
    else:
        print("No pages found.")
        return

    # 去除URL的網頁名稱
    # 例如："/bbs/MobileComm/index7063.html"會得到"/bbs/MobileComm/"
    url_without_name = previousUrl.rsplit(pageName, 1)[0]
    # print(f"url_without_name: {url_without_name}")

    # 最新頁面已經使用上面程式碼顯示，所以下面迴圈內依序顯示上一頁、上二頁...
    # 例如上面已經顯示index.html內容，假設總頁碼為7064，接下來要顯示index7063.html, index7062.html...
    # number為欲顯示的頁面總數，因為最新頁面已經顯示，接下來要顯示的頁面數為"number-1"
    for i in range(number - 1):
        # 迴圈第一次時pageNumber為上一頁頁碼，i則為0，代表要顯示上一頁內容
        # 例如"pageNumber - i"為"7063 - 0"，代表要顯示index7063.html
        pageUrl = f"{urlStart}{url_without_name}index{pageNumber - i}.html"
        print(pageUrl)
        response = requests.get(pageUrl, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        content = getPageContent(soup)
        print(content)


# 取得網頁內容
def getPageContent(soup):
    content = ""
    for article in soup.select("div.r-ent"):
        # 取出標題
        title = article.select_one(".title").text.strip()
        # 取出連結
        # 當標題為「本文已被刪除」則<a>為None
        a = article.select_one(".title > a")
        link = a["href"] if a is not None else ""
        # 取出作者
        author = article.select_one(".author").text.strip()
        # 取出日期
        date = article.select_one(".date").text.strip()
        content += "----------------------------------\n"
        content += f"{title}\t{link}\n{author}\t{date}\n"

    return content


def main():
    number = int(input("要顯示幾頁? "))
    bySelect(number)
    print("===================================")
    byPageNumer(number)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
