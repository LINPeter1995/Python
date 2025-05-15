tired = True
headache = True
count = 0

text = "新冠疫苗副作用:\n"
if tired:
    count += 1
    text += f"{count}. 疲倦\n"

if headache:
    count += 1
    text += f"{count}. 頭痛\n"

print(text)
