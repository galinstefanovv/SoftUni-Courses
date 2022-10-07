numbers = int(input())
sum1 = 0
sum2 = 0
for number in range(numbers):
    numbers = int(input())
    if number % 2 == 0:
        sum1 += numbers
    else:
        sum2 += numbers
if sum1 == sum2:
    print(f'Yes')
    print(f'Sum = {sum1}')
else:
    print(f'No')
    print(f'Diff = {abs(sum1 - sum2)}')
