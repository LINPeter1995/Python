import random


def main():
    print("產生1個1~100(含)的整數亂數")
    print(f"random.randint(1, 100): {random.randint(1, 100)}")
    print("-----------------------------------")

    print("產生1個1~100(不含)的整數亂數")
    print(f"random.randrange(1, 100): {random.randrange(1, 100)}")
    print("-----------------------------------")

    print("產生1個2~100(不含)的偶數亂數")
    print(f"random.randrange(2, 100, 2): {random.randrange(2, 100, 2)}")
    print("-----------------------------------")

    print("產生6個1~100(不含)可重複的整數亂數")
    print(f"random.choices(range(1, 100), k=6):\n{
        random.choices(range(1, 100), k=6)}")
    print("-----------------------------------")

    print("產生6個1~100(不含)不重複的整數亂數")
    print(f"random.sample(range(1, 100), k=6):\n{
        random.sample(range(1, 100), k=6)}")
    print("-----------------------------------")

    print("產生1個1~100(含)的浮點亂數")
    print(f"random.uniform(1, 100): {random.uniform(1, 100)}")
    print("-----------------------------------")

    # 浮點數有多位小數，不易重複
    print("產生6個1~100(不含)可重複的浮點亂數")
    print(f"[random.uniform(1, 100) for _ in range(6)]:\n{
        [random.uniform(1, 100) for _ in range(6)]}")
    print("-----------------------------------")

    # 集合類型亂數
    books = ["Python", "C++", "Java", "SQL"]
    print("隨意挑出一個元素")
    print(f"random.choice(books): {random.choice(books)}")
    print("-----------------------------------")

    print("洗牌(隨機重排)")
    random.shuffle(books)
    print(f"random.shuffle(books):\n{books}")


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
