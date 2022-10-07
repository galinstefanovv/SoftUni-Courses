product = input()
weekday = input()
quantity = float(input())
price = 0
if weekday == "Monday" or weekday == "Tuesday" or weekday == "Wednesday" or weekday == "Thursday" or weekday == "Friday":
    if product == "banana":
        price = quantity * 2.50
        print(f'{price:.2f}')
    elif product == "apple":
        price = quantity * 1.20
        print(f'{price:.2f}')
    elif product == "orange":
        price = quantity * 0.85
        print(f'{price:.2f}')
    elif product == "grapefruit":
        price = quantity * 1.45
        print(f'{price:.2f}')
    elif product == "kiwi":
        price = quantity * 2.70
        print(f'{price:.2f}')
    elif product == "pineapple":
        price = quantity * 5.50
        print(f'{price:.2f}')
    elif product == "grapes":
        price = quantity * 3.85
        print(f'{price:.2f}')
    else:
        print("error")
elif weekday == "Saturday" or weekday == "Sunday":
    if product == "banana":
        price = quantity * 2.70
        print(f'{price:.2f}')
    elif product == "apple":
        price = quantity * 1.25
        print(f'{price:.2f}')
    elif product == "orange":
        price = quantity * 0.90
        print(f'{price:.2f}')
    elif product == "grapefruit":
        price = quantity * 1.60
        print(f'{price:.2f}')
    elif product == "kiwi":
        price = quantity * 3
        print(f'{price:.2f}')
    elif product == "pineapple":
        price = quantity * 5.60
        print(f'{price:.2f}')
    elif product == "grapes":
        price = quantity * 4.20
        print(f'{price:.2f}')
    else:
        print("error")
else:
    print("error")

