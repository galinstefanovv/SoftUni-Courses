import sys
flowers = input()
flowers_count = int(input())
budget = int(input())
price = 0
if flowers == "Roses":
    price = flowers_count * 5
    if flowers_count > 80:
        price = price - price * 0.1
elif flowers == "Dahlias":
    price = flowers_count * 3.80
    if flowers_count > 90:
        price = price - price * 0.15
elif flowers == "Tulips":
    price = flowers_count * 2.80
    if flowers_count > 80:
        price = price - price * 0.15
elif flowers == "Narcissus":
    price = flowers_count * 3
    if flowers_count < 120:
        price = price + price * 0.15
elif flowers == "Gladiolus":
    price = flowers_count * 2.5
    if flowers_count < 80:
        price = price + price * 0.2
else:
    sys.exit("Invalid data!")
diff = abs(budget-price)
if budget >= price:
    print(f'Hey, you have a great garden with {flowers_count} {flowers} and {diff:.2f} leva left.')
else:
    print(f'Not enough money, you need {diff:.2f} leva more.')



