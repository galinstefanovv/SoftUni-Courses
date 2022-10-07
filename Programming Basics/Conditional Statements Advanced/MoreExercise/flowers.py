import sys
chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()
price = 0

if season == "Spring" or season == "Summer":
    chrysanthemums_price = 2 * chrysanthemums
    roses_price = 4.10 * roses
    tulips_price = 2.50 * tulips
elif season == "Autumn" or season == "Winter":
    chrysanthemums_price = 3.75 * chrysanthemums
    roses_price = 4.50 * roses
    tulips_price = 4.15 * tulips
else:
    sys.exit("Invalid season!")
price = chrysanthemums_price + roses_price + tulips_price
if holiday == "Y":
    price = price + (price*0.15)
if tulips > 7 and season == "Spring":
    price *= 0.95
elif roses >= 10 and season == "Winter":
    price = price - (price * 0.10)
if chrysanthemums + roses + tulips > 20:
    price = price - (price * 0.2)
print(f'{price + 2:.2f}')