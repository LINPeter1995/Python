import hashlib
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


def calculateHash(jsonData):
    # 使用"sort_keys=True"會先將JSON資料的key排序後再轉成bytes
    # 這樣可以確保即使每次資料僅有key順序不同，但經過排序後仍會被視為相同資料(hash)
    jsonBytes = json.dumps(jsonData, sort_keys=True).encode("UTF-8")
    # 計算出hash value
    return hashlib.sha256(jsonBytes).hexdigest()


def checkHash(currentHash):
    hashPath = Path("OpenData", "updateHash.txt")
    try:
        with open(hashPath, "r") as file:
            previousHash = file.read().strip()
            if currentHash == previousHash:
                print("資料未更新")
            else:
                print("資料有更新")
                # 將新產生的hash value存檔以便之後比對資料是否更新
                with open(hashPath, 'w') as file:
                    file.write(currentHash)
    except FileNotFoundError:
        print("沒有找到hash value的存檔，將hash value存檔以便之後比對資料是否更新")
        with open(hashPath, "w") as file:
            file.write(currentHash)


def main():
    # 餐飲開放資料JSON格式網址 (說明網址：https://data.gov.tw/dataset/7779)
    url = "https://media.taiwan.net.tw/XMLReleaseALL_public/restaurant_C_f.json"
    jsonData = getJsonData(url)
    currentHash = calculateHash(jsonData)
    checkHash(currentHash)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
