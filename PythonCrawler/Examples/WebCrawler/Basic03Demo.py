import requests
from bs4 import BeautifulSoup
import pandas as pd


def getPageContent():
    # 此頁(index7330.html)有2篇文章被刪除，所以文章連結為空值，用以示範資料整理
    url = "https://www.ptt.cc/bbs/MobileComm/index7330.html"
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"請求失敗，status code: {response.status_code}")
        return
    # 建立BeautifulSoup物件
    soup = BeautifulSoup(response.text, "html.parser")
    articles = []
    for article in soup.select("div.r-ent"):
        # 取出標題
        title = article.select_one(".title").text.strip()
        # 取出連結
        # 當標題為「本文已被刪除」則<a>為空值
        a = article.select_one(".title > a")
        link = a["href"] if a else None
        # 取出作者
        author = article.select_one(".author").text.strip()
        # 取出日期
        date = article.select_one(".date").text.strip()

        # print(f"{title}\t{link}\n{author}\t{date}")
        # print("----------------------------------")
        # 將每篇文章內容先存放至list
        list = [title, link, author, date]
        articles.append(list)

    # 將整頁所有文章轉存放至DataFrame
    df = pd.DataFrame(articles, columns=["title", "link", "author", "date"])
    return df


def dataInfo(df):
    # 列出DataFrame資訊，以查詢哪些欄位有空值
    df.info()
    # 使用dropna()刪除link為空值的文章
    df = df.dropna(subset=["link"])
    print(df)


def main():
    df = getPageContent()
    dataInfo(df)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
