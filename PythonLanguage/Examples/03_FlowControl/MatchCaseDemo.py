# 基本類型、字串比對與or
rating = 5
match rating:
    case 1:
        print("第1名，10,000元獎金")
    case 2:
        print("第2名，5,000元獎金")
    case 3:
        print("第3名，2,000元獎金")
    # 可以使用as來取得對應值
    case (4 | 5) as number:
        print(f"佳作(第{number}名)，500元獎金")
    case _:
        print("還要再努力")

# Tuple比對
niceSeasons = ("spring", "autumn")
match niceSeasons:
    case ("summer", "winter"):
        print("冷熱分明季節")
    case ("spring", "autumn"):
        print("溫和季節")
