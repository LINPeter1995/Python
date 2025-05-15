# 題目：河內塔 (Tower of Hanoi)
# - 有 a, b, c 三根柱，n 個圓盤(由使用者輸入) 放在 a 柱，要將所有圓盤從 a 柱移動到 c 柱
# - 計算總共移動幾次
# 條件：
# - 柱子的小圓盤在上，大圓盤在下
# - 圓盤可移動到任一根柱子
# - 每次只能移動一個圓盤, 而且只能從最上面圓盤開始移動

# 將n個圓盤由source搬運到destination
def move(n, source, auxiliary, destination):
    count = 0
    if n == 1:
        print(source + " -> " + destination)
        count += 1
    else:
        # 將n-1個圓盤由source搬到auxiliary
        count += move(n - 1, source, destination, auxiliary)
        # 將1個圓盤由source搬到destination
        count += move(1, source, auxiliary, destination)
        # 再將n-1個圓盤由auxiliary搬到destination
        count += move(n - 1, auxiliary, source, destination)
    return count

    #  呼叫式為move(3, "a", "b", "c")可拆解成下列呼叫式
    # 	move(2, "a", "c", "b");
    # 	  move(1, "a", "b", "c"); a -> c
    # 	  move(1, "a", "c", "b"); a -> b
    # 	  move(1, "c", "a", "b"); c -> b
    # 	move(1, "a", "b", "c"); a -> c
    # 	move(2, "b", "a", "c");
    # 	  move(1, "b", "c", "a"); b -> a
    # 	  move(1, "b", "a", "c"); b -> c
    # 	  move(1, "a", "b", "c"); a -> c


def main():
    n = int(input("圓盤數量: "))
    # 搬運次數
    count = move(n, "a", "b", "c")
    print(f"搬運次數: {count}")


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
