import os
from datetime import datetime


def showHomeDir():
    print("顯示使用者家目錄資訊:")
    # 取得使用者家目錄
    # "~"或"~user"代表指定使用者家目錄
    userHome = os.path.expanduser("~")
    print(f"user's home directory: {userHome}")
    print(f"parent directory path: {os.path.dirname(userHome)}")
    print(f"isfile: {os.path.isfile(userHome)}")
    print(f"isdir: {os.path.isdir(userHome)}")
    print(f"create time: {datetime.fromtimestamp(os.path.getctime(userHome))}")
    print("listdir(): " + ", ".join(os.listdir(userHome)))


def fileManage():
    userHome = os.path.expanduser("~")
    print("建立目錄")
    dir1 = f"{userHome}/testDir/dir1"
    if os.path.exists(dir1):
        print(f"{dir1} exists")
    else:
        # 路徑中所有不存在的目錄都會建立
        os.makedirs(dir1)
        print(f"{dir1} is created")
    print("-----------------------------------")

    print("建立檔案")
    file1 = f"{userHome}/testDir/dir1/file1.txt"
    # 檔案不存在時會建立，檔案已存在時會覆蓋
    with open(file1, "w", encoding="UTF-8") as f:
        f.write("Hello")
    print(f"{file1} is created")
    print("-----------------------------------")

    print("檔案搬移兼更名")
    file2 = f"{userHome}/testDir/file2.txt"
    os.rename(file1, file2)
    print(f"{file1}\nis renamed to\n{file2}")
    print("-----------------------------------")

    print("刪除檔案")
    if os.path.exists(file2):
        os.remove(file2)
        print(f"{file2} is removed")
    print("-----------------------------------")

    print("刪除dir1目錄")
    if os.path.exists(dir1) and os.path.isdir(dir1):
        os.rmdir(dir1)
        print(f"{dir1} is removed")
    print("-----------------------------------")

    print("刪除testDir目錄")
    testDir = os.path.dirname(dir1)
    if os.path.exists(testDir):
        os.rmdir(testDir)
        print(f"{testDir} is removed")


def main():
    showHomeDir()
    print("===================================")
    fileManage()


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
