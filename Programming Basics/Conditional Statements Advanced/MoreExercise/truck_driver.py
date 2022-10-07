season = input()
km_month = float(input())
price = 0
if km_month <= 5000:
    if season == "Spring" or season == "Autumn":
        price = km_month * 0.75
    elif season == "Summer":
        price = km_month * 0.90
    elif season == "Winter":
        price = km_month * 1.05
    else:
        print("Invalid data!")
elif 5000 < km_month <= 10000:
    if season == "Spring" or season == "Autumn":
        price = km_month * 0.95
    elif season == "Summer":
        price = km_month * 1.10
    elif season == "Winter":
        price = km_month * 1.25
    else:
        print("Invalid data!")
elif 10000 < km_month <= 20000:
    price = km_month * 1.45

price = price - (price * 0.1)

print(f'{price * 4:.2f}')