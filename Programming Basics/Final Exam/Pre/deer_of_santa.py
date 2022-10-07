from math import ceil, floor
absence = int(input())
food_left = int(input())
food_first = float(input()) * absence
food_second = float(input()) * absence
food_third = float(input()) * absence
total = food_first + food_second + food_third
diff = abs(total - food_left)
if total <= food_left:
    print(f'{floor(diff)} kilos of food left.')
else:
    print(f'{ceil(diff)} more kilos of food are needed.')
