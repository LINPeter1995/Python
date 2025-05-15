import requests
from bs4 import BeautifulSoup


def main():
    url = "https://www.ptt.cc/bbs/Gossiping/index.html"
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"請求失敗，status code: {response.status_code}")
        return
    print(response.text)
    # 跟之前去PTT手機版不同，八卦版會檢查是否有點擊滿18歲的按鈕，如果沒有會導至同意畫面，而無法進一步取得文章資料
    # 使用Chrome開發者工具查看"我同意"頁面的：
    # Payload: from: /bbs/Gossiping/index.html
    # Cookies: 沒有"over18=1"
    # 原始碼: 觀察"input type="hidden"標籤與"button name="yes"按鈕
    # 下個範例-Cookies02Demo，會說明解決方式


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")

