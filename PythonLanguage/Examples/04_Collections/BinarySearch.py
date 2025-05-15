def binarySearch(numbers, target):
    start = 0
    end = len(numbers) - 1
    while start <= end:
        mid = (start + end) // 2
        if target == numbers[mid]:
            return mid
        elif target > numbers[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1


def main():
    # 將輸入的數列拆解成整數後存入list
    numbers = list(map(int, input("輸入數列: ").split()))

    # 欲搜尋數字
    target = int(input("搜尋數字: "))
    # 二元搜尋法要先排序完畢，可以自行撰寫排序程式，也可以直接使用函式庫
    numbers.sort()
    print("排序完畢: ", end="")
    for number in numbers:
        print(number, end=" ")
    print()

    # 數列已經排序過，找到會輸出該數索引，否則回傳-1
    result = binarySearch(numbers, target)
    print(f"搜尋結果: {result}")


main()
