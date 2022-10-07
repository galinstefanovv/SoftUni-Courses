budget = float(input())
season = input()
price = 0
destination = ""
typ = ""
if season == "summer" or season == "winter":
    if budget <= 100:
        destination = "Bulgaria"
        if season == "summer":
            price = budget * 0.3
            typ = "Camp"
        elif season == "winter":
            price = budget * 0.7
            typ = "Hotel"
    elif 100 < budget <= 1000:
        destination = "Balkans"
        if season == "summer":
            price = budget * 0.4
            typ = "Camp"
        elif season == "winter":
            price = budget * 0.8
            typ = "Hotel"
    else:
        destination = "Europe"
        typ = "Hotel"
        price = budget * 0.9
else:
    print("Invalid data!")
print(f'Somewhere in {destination}')
print(f'{typ} - {price:.2f}')