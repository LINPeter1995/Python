#⼤樂透號碼總共有 6 個號碼加 1 個特別號，⽽且都不重複 
#利⽤亂數產⽣⼀組⼤樂透號碼，除了特別號以外，其他 6 個號碼由⼩到⼤排序 
#⼤樂透號碼都是1~49，可使⽤ random.randint(1, 49) 產⽣
#開獎，⼤樂透號碼為:  
#38 11 43 13 15 23 特別號: 29 
#由⼩到⼤排列: 
#11 13 15 23 38 43 特別號: 29
import random

# 用來儲存已產生的隨機數字
random_numbers = []

# 產生 6 個不重複的隨機數字
while len(random_numbers) < 6:
    num = random.randint(1, 49)
    if num not in random_numbers:
        random_numbers.append(num)

print("6 個不重複的隨機數字是:", random_numbers)







