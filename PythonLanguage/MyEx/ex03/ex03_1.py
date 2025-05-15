#假設⼀趟泰國之旅需要 20000 元與 5 天的假期。讓使⽤者輸入⾝
#上的錢與放假天數，並顯⽰對應結果
#⾝上的錢: 20000
#放假天數: 5 
#可以去泰國玩
# 錢 >= 2000假期 >= 5列印結果
# True True可以去泰國玩
# True False有錢沒閒
# False True有閒沒錢
# False False沒錢沒閒,真可憐
money = int(input("⾝上的錢: "))
day = int(input("放假天數: "))

# 條件判斷
if money >= 20000 and day >= 5:
    print("可以去泰國玩")
elif money >= 20000:
    print("有錢沒閒")
elif day >= 5:
    print("有閒沒錢")
else:
    print("沒錢沒閒，真可憐")

