# 站名: 台中
# 緯度: 24.111111
# 經度: 121.111111
# 站名: 台中, 緯度: 24.111111, 經度: 121.111111
# 繼續輸入 ( Y | y ):  y

# 站名: 台中
# 緯度: 24.111111
# 經度: 121.111111
# 台中站已經存在

# 站名: 台北
# 緯度: 24.333333
# 經度: 121.111111
# 站名: 台北, 緯度: 24.333333, 經度: 121.111111
# 繼續輸入 ( Y | y ):  y

# 站名: 桃園
# 緯度: 24.222222
# 經度: 121.111111
# 站名: 桃園, 緯度: 24.222222, 經度: 121.111111
# 繼續輸入 ( Y | y ):  n

# ⾞站依照緯度⾼到低排序如下:
# 站名: 台北, 緯度: 24.333333, 經度: 121.111111
# 站名: 桃園, 緯度: 24.222222, 經度: 121.111111
# 站名: 台中, 緯度: 24.111111, 經度: 121.111111

class Station:
    def __init__(self, name=str, latitude=float, longitude=float):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    # 站名不可重複
    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    # 輸出車站信息
    def __str__(self):
        return f"站名: {self.name}, 緯度: {self.latitude}, 經度: {self.longitude}"


def main():
    stations = []  # 用來存儲車站
    while True:
        # 請使用者輸入車站名稱、緯度、經度
        name = input("請輸入站名: ")
        latitude = float(input("請輸入緯度: "))
        longitude = float(input("請輸入經度: "))

        # 檢查車站名稱是否重複
        new_station = Station(name, latitude, longitude)
        if new_station in stations:
            print(f"{name} 站已經存在")
        else:
            stations.append(new_station)

        # 繼續輸入車站信息
        continue_input = input("繼續輸入 ( Y | N ): ").lower()
        if continue_input != 'y':
            break

    # 依照緯度從高到低排序
    stations.sort(key=lambda station: station.latitude, reverse=True)

    # 顯示排序後的車站資訊
    print("\n⾞站依照緯度⾼到低排序如下: ")
    for station in stations:
        print(station)


if __name__ == "__main__":
    main()
