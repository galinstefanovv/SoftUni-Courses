import sys
budget = int(input())
season = input()
fishermen = int(input())
price = 0
if season == "Spring":
    price = 3000
elif season == "Summer" or season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600
else:
    sys.exit("Invalid season!")
if fishermen <= 6:
    price = price - price * 0.1
elif 7 <= fishermen <= 11:
    price = price - price * 0.15
elif fishermen > 12:
    price = price - price * 0.25

if season != "Autumn" and fishermen % 2 == 0:
    price = price - price * 0.05
diff = abs(budget - price)
if budget >= price:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {diff:.2f} leva.')

