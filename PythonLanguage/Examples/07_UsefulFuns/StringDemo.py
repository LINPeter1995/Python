def main():
    myStr = "Hello "
    print(f"myStr: {myStr}")
    print(f"len(myStr): {len(myStr)}")
    # 取值
    print(f"myStr[1]: {myStr[1]}")
    print(f"myStr[2:5]: {myStr[2:5]}")
    print(f"myStr.index('l'): {myStr.index('l')}")
    # 比值
    print(f"myStr == 'HELLO ': {myStr == 'HELLO '}")
    print(f"myStr.startswith('He'): {myStr.startswith('He')}")
    print(f"myStr.endswith('lo'): {myStr.endswith('lo')}")
    print(f"'Hello' in myStr: {'Hello' in myStr}")
    # 改值
    print(f"myStr.upper(): {myStr.upper()}")
    print(f"myStr.lower(): {myStr.lower()}")
    print(f"myStr.strip(): {myStr.strip()}")
    print(f"myStr.replace('l', 'o'): {myStr.replace('l', 'o')}")
    # immutable，原字串實例內容未變
    print(f"myStr: {myStr}")


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
