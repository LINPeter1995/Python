import requests
from bs4 import BeautifulSoup


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
        content += f"{title}\t{link}\n{author}\t{date}\n"
        content += "----------------------------------\n"

    return content


# 開啟 Chrome 開發人員工具，觀察點擊「我同意，我已年滿十八歲」的結果
# Network > Payload 記錄送出資訊 "from" 與 "yes" 參數與值
# Network > Cookies 記錄 Response Cookies 有 "over18=1" 資訊
# 之後再次進入八卦版，Request Cookies 就會帶有 "over18=1" 資訊，也不再有要求同意的畫面
def main():
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}

    # session會儲存發送請求後收到的cookies資訊，方便再次送出請求時可以將儲存的cookies再次送出
    session = requests.Session()
    # 是否滿18頁面
    over18Url = "https://www.ptt.cc/ask/over18"
    # 要將hidden、「我同意」按鈕參數名稱與值包成POST請求的data
    # 換句話說就是用程式模擬使用者按下同意鈕的結果
    data = {
        "from": "/bbs/Gossiping/index.html",
        "yes": "yes"
    }
    # 送出POST請求後server會回傳cookies：「over18=1」，並且會儲存至session
    session.post(over18Url, headers=headers, data=data)
    # 因為session內儲存「over18=1」，之後每次以session發出請求，server都會知道已滿18歲，所以會回傳文章資訊
    response = session.get("https://www.ptt.cc/bbs/Gossiping/index.html")
    if response.status_code != 200:
        print(f"請求失敗，status code: {response.status_code}")
        return
    soup = BeautifulSoup(response.text, "html.parser")
    content = getPageContent(soup)
    print(content)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
