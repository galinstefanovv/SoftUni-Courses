money = float(input())
year = int(input())
age = 18
for living in range(1800, year + 1):
    if living % 2 == 0:
        money -= 12000
    else:
        money -= 12000 + 50 * age
    age += 1

if money >= 0:
    print(f'Yes! He will live a carefree life and will have {money:.2f} dollars left.')
else:
    print(f'He will need {abs(money):.2f} dollars to survive.')