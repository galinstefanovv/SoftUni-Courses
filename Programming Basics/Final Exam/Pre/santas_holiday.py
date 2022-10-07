days = int(input())
type = input()
feedback = input()
total = 0
nights = days - 1
if type == "room for one person":
    total = nights * 18
elif type == "apartment":
    total = nights * 25
    if days < 10:
        total *= 0.7
    elif 10 <= days <= 15:
        total *= 0.65
    else:
        total *= 0.5
elif type == "president apartment":
    total = nights * 35
    if days < 10:
        total *= 0.9
    elif 10 <= days <= 15:
        total *= 0.85
    else:
        total *= 0.8
else:
    print("Invalid data!")
if feedback == "positive":
    total += total * 0.25
elif feedback == "negative":
    total *= 0.9
print(f'{total:.2f}')