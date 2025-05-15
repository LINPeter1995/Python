score = 87
text = f"{score}分，"

if score >= 85:
    text += "贏得10,000元獎學金！\n"
elif score >= 75:
    text += "贏得5,000元獎學金！\n"
else:
    text += "再努力！\n"

print(text)
