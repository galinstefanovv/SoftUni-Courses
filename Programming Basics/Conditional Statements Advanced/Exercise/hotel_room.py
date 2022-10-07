import sys
month = input()
overnight = int(input())
apartment = 0
studio = 0
if month == "May" or month == "October":
    studio = 50
    apartment = 65
    if overnight > 14:
        studio *= 0.7
    elif overnight > 7:
        studio *= 0.95
elif month == "June" or month == "September":
    studio = 75.2
    apartment = 68.7
    if overnight > 14:
        studio *= 0.8
elif month == "July" or month == "August":
    studio = 76
    apartment = 77
else:
    sys.exit("Invalid data!")
if overnight > 14:
    apartment *= 0.9
print(f'Apartment: {overnight * apartment:.2f} lv.')
print(f'Studio: {overnight * studio:.2f} lv.')
