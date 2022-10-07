from math import floor, ceil
days = int(input())
food_left = int(input())
dog_food_days = float(input())
cat_food_days = float(input())
turtle_food_days = float(input())
turtle_food = turtle_food_days / 1000
food_total = dog_food_days + cat_food_days + turtle_food
needed_food = food_total * days
diff = abs(food_left - needed_food)
if food_left >= needed_food:
    print(f'{floor(diff)} kilos of food left.')
else:
    print(f'{ceil(diff)} more kilos of food are needed.')