price_travel = float(input())
puzzle = int(input())
doll = int(input())
bear = int(input())
minion = int(input())
truck = int(input())
count = puzzle + doll + bear + minion + truck
total = (puzzle * 2.60) + (doll * 3) + (bear * 4.10) + (minion * 8.20) + (truck * 2)
if count >= 50:
    total = total - (total * 0.25)
rent = total * 0.1
total = total - rent

if total >= price_travel:
    diff = total - price_travel
    print(f'Yes! {diff:.2f} lv left.')
else:
    diff = price_travel - total
    print(f'Not enough money! {diff:.2f} lv needed.')

