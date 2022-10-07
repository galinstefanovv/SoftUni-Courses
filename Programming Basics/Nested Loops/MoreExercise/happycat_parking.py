days = int(input())
hours = int(input())
total = 0
for i in range(1, days + 1):
    tax = 0
    for j in range(1, hours + 1):
        if i % 2 == 0 and j % 2 != 0:
            tax += 2.50
            total += 2.50
        elif i % 2 != 0 and j % 2 == 0:
            tax += 1.25
            total += 1.25
        else:
            tax += 1
            total += 1
    print(f'Day: {i} - {tax:.2f} leva')
print(f'Total: {total:.2f} leva')