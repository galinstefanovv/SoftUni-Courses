budget = float(input())
season = input()
price = 0
place = ""
location = ""
if budget <= 1000:
    place = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.65
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.45
    else:
        print("Invalid data")
elif 1000 < budget <= 3000:
    place = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.8
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.6
    else:
        print("Invalid data")
elif budget > 3000:
    place = "Hotel"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.9
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.9
    else:
        print("Invalid data")
print(f'{location} - {place} - {price:.2f}')
