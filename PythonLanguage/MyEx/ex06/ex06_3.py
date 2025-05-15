# 承襲 6-1，但再建立 1 個長⽅體類別的⼦類別：房屋 (House) 類別，內容包含 
# 屬性：增加材質 (material) 屬性 
# ⽅法：覆寫getInfo()⽅法：除了回傳長、寬、⾼與體積外，還能回傳材質 
# 建構式：設定長、寬、⾼、材質等 4 屬性的初始值 
# 主流程 
# 詢問使⽤者欲輸入的房屋總個數 
# 讓使⽤者輸入指定個數的房屋資訊，並顯⽰所有輸入房屋的長、寬、⾼與體積
# 請問有幾間房屋? 3 
# 請輸入第1間房屋的長、寬、⾼與材質(空⽩間隔): 1 1 1 C 
# 請輸入第2間房屋的長、寬、⾼與材質(空⽩間隔): 2 2 2 B 
# 請輸入第3間房屋的長、寬、⾼與材質(空⽩間隔): 3 3 3 A 
# 輸入的3間房屋資訊如下: 
# 長: 1.0, 寬: 1.0, ⾼: 1.0, 體積: 1.0, 材質: C 
# 長: 2.0, 寬: 2.0, ⾼: 2.0, 體積: 8.0, 材質: B 
# 長: 3.0, 寬: 3.0, ⾼: 3.0, 體積: 27.0, 材質: A

# 定義長方體類別
class Cuboid:
    def __init__(self, length, width, height):
        self.length = float(length)
        self.width = float(width)
        self.height = float(height)

    def volume(self):
        return self.length * self.width * self.height

    def getInfo(self):
        # 回傳長、寬、高與體積
        volume = self.volume()
        return f"長: {self.length}, 寬: {self.width}, 高: {self.height}, 體積: {volume}"

# 定義房屋類別，繼承自長方體類別
class House(Cuboid):
    def __init__(self, length, width, height, material):
        # 呼叫父類別的建構式初始化長、寬、高
        super().__init__(length, width, height)
        self.material = material

    def getInfo(self):
        # 覆寫 getInfo() 方法，回傳長、寬、高、體積與材質
        Override = super().getInfo()  # 呼叫父類別的 getInfo()
        return f"{Override}, 材質: {self.material}"

# 主流程
def main():
    # 詢問使用者欲輸入的房屋總個數
    num_houses = int(input("請問有幾間房屋? "))
    
    houses = []
    for i in range(1, num_houses + 1):
        # 讓使用者輸入房屋資訊
        data = input(f"請輸入第{i}間房屋的長、寬、高與材質(空白間隔): ").split()
        length, width, height, material = data
        # 建立房屋物件
        house = House(length, width, height, material)
        houses.append(house)

    # 顯示所有輸入房屋的長、寬、高、體積與材質
    print(f"輸入的{num_houses}間房屋資訊如下: ")
    for house in houses:
        print(house.getInfo())

# 執行主流程
if __name__ == "__main__":
    main()
