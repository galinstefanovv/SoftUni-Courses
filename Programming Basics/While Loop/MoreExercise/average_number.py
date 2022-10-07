n = int(input())
sum = 0
count = 0
for i in range(1, n + 1):
    n = int(input())
    count += 1
    sum += n
average = sum / count
print(f'{average:.2f}')