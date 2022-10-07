budget = float(input())
season = input()
price = 0
class_type = ""
car_type = ""
if budget <= 100:
    class_type = "Economy class"
    if season == "Summer":
        car_type = "Cabrio"
        price = budget * 0.35
    elif season == "Winter":
        car_type = "Jeep"
        price = budget * 0.65
    else:
        print("Invalid data")
elif 100 < budget <= 500:
    class_type = "Compact class"
    if season == "Summer":
        car_type = "Cabrio"
        price = budget * 0.45
    elif season == "Winter":
        car_type = "Jeep"
        price = budget * 0.80
    else:
        print("Invalid data")
elif budget > 500:
    class_type = "Luxury class"
    if season == "Summer" or season == "Winter":
        car_type = "Jeep"
        price = budget * 0.90
    else:
        print("Invalid data")

print(f'{class_type}')
print(f'{car_type} - {price:.2f}')