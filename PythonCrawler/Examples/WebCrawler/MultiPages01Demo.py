import re
import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/MobileComm/index.html"
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}
# 網站起始url
urlStart = "https://www.ptt.cc"


def previousPageUrl(pageUrl):
    response = requests.get(pageUrl, headers=headers)
    if response.status_code != 200:
        print(f"請求失敗，status code: {response.status_code}")
        return
    soup = BeautifulSoup(response.text, "html.parser")
    # 先使用Chrome觀察如何取得上頁連結
    links = soup.select("div.btn-group.btn-group-paging a")
    # 因為上頁連結排在第2個，所以index為1
    return links[1]["href"]


def bySelect():
    pageUrl = url
    # 顯示本頁與前2頁個別頁面的url
    for i in range(3):
        print(pageUrl)
        pageUrl = urlStart + previousPageUrl(pageUrl)


def byPageNumer():
    # 最新頁面
    print(url)

    # 最新頁面為index.html，沒有頁碼，先取得上一頁連結並觀察頁碼
    previousUrl = previousPageUrl(url)

    # 去除URL的分隔符號"/" (+ 代表1個以上) 後會得到list，最後一個元素為網頁檔名
    # 例如："/bbs/MobileComm/index7063.html" 會得到"index7063.html"
    pageName = re.compile(r"/+").split(previousUrl)[-1]
    # print(f"pageName: {pageName}")

    # 尋找網頁檔名中含有的數字，也就是頁碼
    # 例如："index7063.html"會得到"7063"。re沒有find_one()可用
    numbers = re.findall(r"[0-9]+", pageName)
    # 檢查是否有頁碼
    if numbers:
        pageNumber = int(numbers[0])
        # print(f"pageNumber: {pageNumber}")
    else:
        print("No pages found.")
        return

    # 上一頁
    print(f"{urlStart}{previousUrl}")

    # 去除URL的網頁名稱使用rsplit(right split: 從右(末)端開始移除)
    # rsplit(pageName, 1)，1:去除1個，代表從末端開始找，符合的第1個會被去除
    # 例如："/bbs/MobileComm/index7063.html"會得到"/bbs/MobileComm/"
    url_without_name = previousUrl.rsplit(pageName, 1)[0]
    # print(f"url_without_name: {url_without_name}")

    # 上二頁
    print(f"{urlStart}{url_without_name}index{pageNumber - 1}.html")


def main():
    bySelect()
    print("---------------------------------")
    byPageNumer()


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")

