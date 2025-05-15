from pathlib import Path
from PIL import Image


def demoReadImage(file):
    print("讀取圖檔並顯示相關訊息:")
    with Image.open(file) as image:
        print(f"image.format: {image.format}")
        print(f"image.size: {image.size}")
        print(f"image.mode: {image.mode}")
        image.show()


def demoReadWriteImage(source, destination):
    print("同時讀寫圖檔資料")
    with Image.open(source) as image:
        image.save(destination)


def demoImageProcess(file):
    with Image.open(file) as image:
        print("影像大小調整: 200x200")
        resized_image = image.resize((200, 200))
        resized_image.show()

        print("旋轉影像: 順時針旋轉45度")
        rotated_image = image.rotate(45)
        rotated_image.show()

        print("轉為灰階")
        # "L" - grayscale
        gray_image = image.convert("L")
        gray_image.show()

        print("影像裁切")
        # 裁切區域 (左, 上, 右, 下)
        cropped_image = image.crop((50, 50, 200, 200))
        cropped_image.show()


def main():
    readDir = Path("09_FileIO", "read")
    writeDir = Path("09_FileIO", "write")
    # 存放目錄不存在就建立，相對路徑代表存放位置跟執行的Python檔案放在同一目錄
    writeDir.mkdir(exist_ok=True)

    demoReadImage(readDir/"image.png")
    print("-----------------------------------")
    demoReadWriteImage(readDir/"image.png", writeDir/"image.png")
    print("-----------------------------------")
    demoImageProcess(readDir/"image.png")


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
