#建立 1 個長⽅體 (Cuboid) 類別，內容包含 
#屬性：長 (length)、寬 (width)、⾼ (height) 
#⽅法  
#volume() ⽅法：計算完體積並回傳 
#getInfo() ⽅法：回傳長、寬、⾼與體積 
#建構式：設定屬性初始值 
#主流程 
#將使⽤者輸入的長、寬、⾼建立 Cuboid 物件，並顯⽰該物件長、寬、⾼與體積
######請輸入長⽅體的長、寬、⾼(空⽩間隔): 1 2 3 
######輸入的長⽅體資訊如下:  
######長: 1.0, 寬: 2.0, ⾼: 3.0, 體積: 6.0
class Cuboid:
    def __init__(self, length, width, height):
        # 建構式，用來初始化屬性
        self.length = float(length)
        self.width = float(width)
        self.height = float(height)
    
    def volume(self):
        # 計算體積
        return self.length * self.width * self.height
    
    def getInfo(self):
        # 返回長、寬、高與體積
        volume = self.volume()
        return f"長: {self.length}, 寬: {self.width}, 高: {self.height}, 體積: {volume}"

# 主流程
def main():
    # 讓使用者輸入長、寬、高
    length, width, height = input("請輸入長方體的長、寬、高(空白間隔): ").split()
    
    # 創建 Cuboid 物件
    cuboid = Cuboid(length, width, height)
    
    # 顯示長方體資訊
    print(f"輸入的長方體資訊如下:")
    print(cuboid.getInfo())

# 執行主流程
if __name__ == "__main__":
    main()
