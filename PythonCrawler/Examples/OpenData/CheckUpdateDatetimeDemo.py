import json
import requests
from pathlib import Path


def getJsonData(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"請求失敗，status code: {response.status_code}")
        return
    try:
        # 如果資料內容為JSON格式，可直接呼叫json()
        jsonData = response.json()
    except json.decoder.JSONDecodeError:
        # 此網站使用"utf-8-sig"編碼，需要標註內容使用"utf-8-sig"編碼，
        # 否則產生"JSONDecodeError("Unexpected UTF-8 BOM (decode using utf-8-sig)"錯誤
        response.encoding = "utf-8-sig"
        jsonData = response.json()

    return jsonData


def getUpdateDateTime(jsonData):
    datetime = jsonData["XML_Head"]["Updatetime"]
    return datetime


def checkDatetime(currentDateTime):
    datetimePath = Path("OpenData", "updateDatetime.txt")
    try:
        with open(datetimePath, "r") as file:
            previousDateTime = file.read().strip()
            # 新舊日期時間字串比對
            if currentDateTime == previousDateTime:
                print("資料未更新")
            else:
                print("資料有更新")
                # 將新產生的日期時間存檔以便之後比對資料是否更新
                with open(datetimePath, 'w') as file:
                    file.write(currentDateTime)
    except FileNotFoundError:
        print("沒有找到datetime的存檔，將datetime存檔以便之後比對資料是否更新")
        with open(datetimePath, "w") as file:
            file.write(currentDateTime)


def main():
    # 餐飲開放資料JSON格式網址 (說明網址：https://data.gov.tw/dataset/7779)
    url = "https://media.taiwan.net.tw/XMLReleaseALL_public/restaurant_C_f.json"
    jsonData = getJsonData(url)
    currentDateTime = getUpdateDateTime(jsonData)
    print(f"currentDateTime: {currentDateTime}")
    checkDatetime(currentDateTime)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
