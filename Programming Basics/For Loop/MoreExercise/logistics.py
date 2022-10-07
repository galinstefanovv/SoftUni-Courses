cargo = int(input())
total = 0
price = 0
minibus_p = 0
truck_p = 0
train_p = 0
for tons in range(1, cargo + 1):
    ton = int(input())
    total += ton
    if ton <= 3:
        minibus_p += ton
    elif 4 <= ton <= 11:
        truck_p += ton
    elif ton >= 12:
        train_p += ton
minibus = minibus_p / total * 100
truck = truck_p / total * 100
train = train_p / total * 100
average_price = (minibus_p * 200 + truck_p * 175 + train_p * 120) / total
print(f'{average_price:.2f}')
print(f'{minibus:.2f}%')
print(f'{truck:.2f}%')
print(f'{train:.2f}%')