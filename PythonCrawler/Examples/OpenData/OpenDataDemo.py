import json
import requests
import pandas as pd


def main():
    # 餐飲開放資料JSON格式網址 (說明網址：https://data.gov.tw/dataset/7779)
    url = "https://media.taiwan.net.tw/XMLReleaseALL_public/restaurant_C_f.json"
    response = requests.get(url)
    # 檢查request是否成功，如果成功status code為200
    if response.status_code != 200:
        print(f"請求失敗，status code: {response.status_code}")
        return
    try:
        # 如果資料內容為JSON格式，可直接呼叫json()
        jsonData = response.json()
    except json.decoder.JSONDecodeError:
        # 此網站使用"utf-8-sig"編碼，需要標註內容使用"utf-8-sig"編碼，
        # 否則產生"JSONDecodeError("Unexpected UTF-8 BOM (decode using utf-8-sig)"錯誤
        response.encoding = 'utf-8-sig'
        jsonData = response.json()

    # 確定jsonData資料類型，以決定如何進一步取資料內容方式
    print(f"type(jsonData): {type(jsonData)}")
    print("-----------------------------------")
    infoList = jsonData["XML_Head"]["Infos"]["Info"]
    # 將資料轉成DataFrame
    df = pd.DataFrame(infoList)

    print("DataFrame info:")
    df.info()
    print("-----------------------------------")

    print("DataFrame head:")
    print(df.head())


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
