import sys
days = int(input()) - 1
type_room = input()
rating = input()
price = 0
discount = 0
if type_room == "room for one person":
    price = days * 18
elif type_room == "apartment":
    price = days * 25
    if days < 10:
        price = price - (price * 0.3)
    elif 10 <= days <= 15:
        price = price - (price * 0.35)
    else:
        price = price - (price * 0.5)
elif type_room == "president apartment":
    price = days * 35
    if days < 10:
        price = price - (price * 0.1)
    elif 10 <= days <= 15:
        price = price - (price * 0.15)
    else:
        price = price - (price * 0.2)
else:
    sys.exit("Invalid data")
if rating == "positive":
    price = price + (price * 0.25)
elif rating == "negative":
    price = price - (price * 0.1)
else:
    sys.exit("Invalid data")

print(f'{price:.2f}')