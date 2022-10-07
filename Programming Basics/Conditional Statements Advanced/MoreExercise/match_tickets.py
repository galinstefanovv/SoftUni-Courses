budget = float(input())
category = input()
people = int(input())
price = 0
vip_price = people * 499.99
norm_price = people * 249.99
if 1 <= people <= 4:
    price = budget * 0.75
elif 5 <= people <= 9:
    price = budget * 0.6
elif 10 <= people <= 24:
    price = budget * 0.5
elif 25 <= people <= 49:
    price = budget * 0.4
else:
    price = budget * 0.25
diff = abs(budget - price)
if category == "VIP":
    if diff >= vip_price:
        print (f'Yes! You have {abs(diff - vip_price):.2f} leva left.')
    else:
        print (f'Not enough money! You need {abs(vip_price - diff):.2f} leva.')
elif category == "Normal":
    if diff >= norm_price:
        print (f'Yes! You have {abs(diff - norm_price):.2f} leva left.')
    else:
        print (f'Not enough money! You need {abs(norm_price - diff):.2f} leva.')
else:
    print("Invalid data.")

