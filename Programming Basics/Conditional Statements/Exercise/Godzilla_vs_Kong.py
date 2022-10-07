budget = float(input())
extra = int(input())
suit_price = float(input())
decor = budget * 0.1
if extra > 150:
    suit_price = suit_price - (suit_price * 0.1)
total = decor + (extra * suit_price)
if total > budget:
    diff = total - budget
    print("Not enough money!")
    print(f'Wingard needs {diff:.2f} leva more.')
else:
    diff = budget - total
    print("Action!")
    print(f'Wingard starts filming with {diff:.2f} leva left.')