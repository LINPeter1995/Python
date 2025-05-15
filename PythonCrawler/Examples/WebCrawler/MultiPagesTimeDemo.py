import time
import requests
from bs4 import BeautifulSoup


def main():
    url = "https://www.ptt.cc/bbs/MobileComm/index.html"
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}
    # 網站起始url
    urlStart = "https://www.ptt.cc"

    number = int(input("要顯示幾頁? "))
    for i in range(number):
        print(url)
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"請求失敗，status code: {response.status_code}")
            return
        soup = BeautifulSoup(response.text, "html.parser")
        # 取得上頁連結
        link = soup.select("div.btn-group.btn-group-paging a")
        url = urlStart + link[1]["href"]
        # 停3秒後繼續
        time.sleep(3)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")

