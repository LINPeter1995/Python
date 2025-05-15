import re
import requests
from bs4 import BeautifulSoup
from pathlib import Path
import pandas as pd


# 取得網頁內容
def addPageContent(articles, soup):
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
        # 將每篇文章內容先存放至list
        list = [title, link, author, date]
        articles.append(list)

    # 加完此頁所有文章後回傳articles，方便繼續加入下頁文章
    return articles


def main():
    url = "https://www.ptt.cc/bbs/MobileComm/index.html"
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}
    # 網站起始url
    urlStart = "https://www.ptt.cc"

    number = int(input("要顯示幾頁? "))
    # 儲存所有文章
    articles = []
    for i in range(number):
        print(url)
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"請求失敗，status code: {response.status_code}")
            return

        soup = BeautifulSoup(response.text, "html.parser")
        # articles存放所有文章，soup存放網頁內容
        articles = addPageContent(articles, soup)

        # 取得上頁連結
        previousPageLink = soup.select("div.btn-group.btn-group-paging a")
        url = urlStart + previousPageLink[1]["href"]
    
    print("-----------------------------------")

    # 將所有文章轉存放至DataFrame
    df = pd.DataFrame(articles, columns=["title", "link", "author", "date"])
    df.info()
    print("-----------------------------------")

    # 指定存檔目錄，不存在就建立
    write_dir = Path("WebCrawler/MultiPagesSaveDemo")
    write_dir.mkdir(exist_ok=True)
    # 存成CSV檔案
    df.to_csv(
        write_dir/"MultiPagesSaveDemo.csv",
        header=True,
        index=False
    )
    # 存成JSON檔案
    df.to_json(
        write_dir/"MultiPagesSaveDemo.json",
        orient="records",
        force_ascii=False
    )
    # 存成Excel檔案
    df.to_excel(
        write_dir/"MultiPagesSaveDemo.xlsx",
        index=False
    )
    print(f"存檔完成")


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
