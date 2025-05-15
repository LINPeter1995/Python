import requests
from bs4 import BeautifulSoup


def main():
    url = "https://www.ptt.cc/bbs/MobileComm/index.html"
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"請求失敗，status code: {response.status_code}")
        return
    # 建立BeautifulSoup物件
    soup = BeautifulSoup(response.text, "html.parser")
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
        print(f"{title}\t{link}\n{author}\t{date}")
        print("----------------------------------")


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")

