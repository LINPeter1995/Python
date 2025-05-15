from pathlib import Path
from datetime import datetime


def showHomeDir():
    print("顯示使用者家目錄資訊:")
    userHome = Path.home()
    print(f"user's home directory: {userHome}")
    print(f"parent directory path: {userHome.parent}")
    print(f"isfile: {userHome.is_file()}")
    print(f"isdir: {userHome.is_dir()}")
    print(
        f"create time: {datetime.fromtimestamp(userHome.stat().st_birthtime)}")
    print(f"change time: {datetime.fromtimestamp(userHome.stat().st_ctime)}")
    print("for each item: " +
          ", ".join([item.name for item in userHome.iterdir()]))


def fileManage():
    userHome = Path.home()
    print("建立目錄:")
    dir1 = userHome/"testDir"/"dir1"
    # parents=True路徑中所有不存在的目錄都會建立
    # 如果該目錄已經存在：
    # exist_ok=False會產生FileExistsError錯誤
    # exist_ok=True則不會產生錯誤
    dir1.mkdir(parents=True, exist_ok=True)
    print(f"{dir1} is created")
    print("-----------------------------------")

    print("建立檔案")
    file1 = userHome/"testDir"/"dir1"/"file1.txt"
    # 檔案不存在時會建立
    if file1.exists():
        print(f"{file1} exists")
    else:
        file1.touch()
        print(f"{file1} is created")
    print("-----------------------------------")

    print("檔案搬移兼更名")
    file2 = userHome/"testDir"/"file2.txt"
    file1.rename(file2)
    print(f"{file1}\nis renamed to\n{file2}")
    print("-----------------------------------")

    print("刪除檔案")
    if file2.exists():
        file2.unlink()
        print(f"{file2} is removed")
    print("-----------------------------------")

    print("刪除dir1目錄")
    if dir1.exists() and dir1.is_dir():
        dir1.rmdir()
        print(f"{dir1} is removed")
    print("-----------------------------------")

    print("刪除testDir目錄")
    testDir = dir1.parent
    if testDir.exists():
        testDir.rmdir()
        print(f"{testDir} is removed")


def main():
    showHomeDir()
    print("===================================")
    fileManage()


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
