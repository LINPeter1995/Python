#使⽤者輸入春、夏、秋、冬任⼀季節，會顯⽰該季節對應描述 
#• 春：春暖花開 
#• 夏：夏⽇炎炎 
#• 秋：秋⾼氣爽 
#• 冬：冬風凜冽
#請輸入你喜愛的季節: 夏 
#夏⽇炎炎

season = input("請輸入你喜愛的季節: ")

match season.lower():
    case "春" | "春天" | "Spring":  # 應該直接與字串"春"進行比較
        print("春暖花開")
    case "夏" | "夏天" | "Summer":  # 你可以添加更多的季節
        print("夏日炎炎")
    case "秋" | "秋天" | "Fall":
        print("秋高氣爽")
    case "冬" | "冬天" | "Winter":
        print("東風凜冽")
    case _:
        print("無效的季節")
