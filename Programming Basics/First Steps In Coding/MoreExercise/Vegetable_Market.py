vegetables = float(input())
fruits = float(input())
vegetables_kg = int(input())
fruits_kg = int(input())
total_lv = (vegetables * vegetables_kg) + (fruits*fruits_kg)
total_eur = total_lv / 1.94
print(f'{total_eur:.2f}')