import sys
degrees = int(input())
time = input()
outfit = ""
shoes = ""

if time == "Morning":
    if 10 <= degrees <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif 18 < degrees <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    else:
        outfit = "T-Shirt"
        shoes = "Sandals"
elif time == "Afternoon":
    if 10 <= degrees <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif 18 < degrees <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
    else:
        outfit = "Swim Suit"
        shoes = "Barefoot"
elif time == "Evening":
    if 10 <= degrees <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif 18 < degrees <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    else:
        outfit = "Shirt"
        shoes = "Moccasins"
else:
    sys.exit("Error! Morning, Afternoon or Evening!")


print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")