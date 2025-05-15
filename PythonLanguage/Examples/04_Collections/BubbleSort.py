def bubbleSort(numbers):
    # i控制要跑幾大回合：5個數排序，只要排好右邊4個即可確定排序，所以「len(numbers) - 1」
    for i in range(len(numbers) - 1):
        swapped = False
        # i值恰代表右側數字已經排好幾個，i=1 代表右側已經排好1個數字(最大值)
        # 既然代表已經排好i個，所以要「-i」，代表右側可少排i個
        for j in range(len(numbers) - 1 - i):
            # 如果左 > 右，兩個元素要交換位置
            if numbers[j] > numbers[j + 1]:
                min = numbers[j + 1]
                numbers[j + 1] = numbers[j]
                numbers[j] = min
                swapped = True

        # 如果這一回合沒有任何元素交換，就代表排序已經確立，
        # 不用再檢查之後元素，所以強制結束迴圈
        if not swapped:
            break

def main():
    # 將輸入的數列拆解成整數後存入list
    numbers = list(map(int, input("輸入數列: ").split()))
    bubbleSort(numbers)
    print("排序完畢: ", end="")
    for number in numbers:
        print(number, end=" ")
    print()

main()
