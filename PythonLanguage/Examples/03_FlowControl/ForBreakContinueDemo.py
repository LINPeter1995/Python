# break
floorStop = 5
for floor in range(1, 11):
    if floor >= floorStop:
        print(f"停在{floor}樓")
        break
    print(f"{floor}樓", end=" ")

# continue
floorSkip = 4
for floor in range(1, 11):
    if floor == floorSkip:
        continue
    print(f"{floor}樓", end=" ")
