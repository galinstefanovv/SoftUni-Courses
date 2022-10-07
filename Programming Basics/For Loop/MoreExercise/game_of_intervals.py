levels = int(input())
points = 0
second = 0
third = 0
fourth = 0
fifth = 0
sixth = 0
seventh = 0
percentage = 0
for i in range(1, levels + 1):
    numbers = int(input())
    if numbers > 50 or numbers < 0:
        points = points / 2
        second += 1
    elif numbers <= 9:
        points += numbers * 0.2
        third += 1
    elif numbers <= 19:
        points += numbers * 0.3
        fourth += 1
    elif numbers <= 29:
        points += numbers * 0.4
        fifth += 1
    elif numbers <= 39:
        points += 50
        sixth += 1
    elif numbers <= 50:
        points += 100
        seventh += 1
print(f'{points:.2f}')
percentage = third / levels * 100
print(f'From 0 to 9: {percentage:.2f}%')
percentage = fourth / levels * 100
print(f'From 10 to 19: {percentage:.2f}%')
percentage = fifth / levels * 100
print(f'From 20 to 29: {percentage:.2f}%')
percentage = sixth / levels * 100
print(f'From 30 to 39: {percentage:.2f}%')
percentage = seventh / levels * 100
print(f'From 40 to 50: {percentage:.2f}%')
percentage = second / levels * 100
print(f'Invalid numbers: {percentage:.2f}%')