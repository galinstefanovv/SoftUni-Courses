from math import floor, ceil
fuel = input()
liters = float(input())
club_card = input()
price = float()
if club_card == "Yes":
    gasoline_d = 2.04
    diesel_d = 2.21
    gas_d = 0.85
else:
    gasoline_d = 2.22
    diesel_d = 2.33
    gas_d = 0.93
if fuel == "Gasoline" or fuel == "Diesel" or fuel == "Gas":
    if fuel == "Gasoline":
        price = liters * gasoline_d
    elif fuel == "Diesel":
        price = liters * diesel_d
    else:
        price = liters * gas_d
else:
    print("Please enter Gasoline, Diesel or Gas!")
if 20 <= liters <= 25:
    price = price - (price * 0.08)
elif liters > 25:
    price = price - (price * 0.1)

print(f'{price:.2f} lv.')

