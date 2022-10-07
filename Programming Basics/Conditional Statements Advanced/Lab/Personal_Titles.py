age = float(input())
gender = str(input())
if gender == "m" or gender == "f":
    if gender == "m" and age >= 16:
        print("Mr.")
    elif gender == "m" and age < 16:
        print("Master")
    elif gender == "f" and age >= 16:
        print("Ms.")
    else:
        print("Miss")
else:
    print("Please enter m or f !")
