score = 85
text = f"{score}分，"

if score >= 85:
    # 需要內縮 4 格，才屬於 if 區塊
    text += "贏得 10,000 元獎學金！\n"
else:
    text += "再努力！\n"

print(text)
