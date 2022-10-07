import sys
juniors = int(input())
seniors = int(input())
route = input()
price = 0
total_js = juniors + seniors
if route == "trail":
    price = (juniors * 5.50) + (seniors * 7)
elif route == "cross-country":
    price = (juniors * 8) + (seniors * 9.50)
    if total_js >= 50:
        price *= 0.75
elif route == "downhill":
    price = (juniors * 12.25) + (seniors * 13.75)
elif route == "road":
    price = (juniors * 20) + (seniors * 21.50)
else:
    sys.exit("Invalid data!")
price *= 0.95
print(f'{price:.2f}')
