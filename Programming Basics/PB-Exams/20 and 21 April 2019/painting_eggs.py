size = input()
color = input()
count = int(input())
price = 0
if size == "Large":
    if color == "Red":
        price += 16
    elif color == "Green":
        price += 12
    elif color == "Yellow":
        price += 9
elif size == "Medium":
    if color == "Red":
        price += 13
    elif color == "Green":
        price += 9
    elif color == "Yellow":
        price += 7
elif size == "Small":
    if color == "Red":
        price += 9
    elif color == "Green":
        price += 8
    elif color == "Yellow":
        price += 5
sum = price * count
tax = sum * 0.35
total = sum - tax

print(f'{total:.2f} leva.')
