first = int(input())
second = int(input())
third = int(input())

for i in range(2, first + 1, 2):
    for j in range(2, second + 1):
        for k in range(2, third + 1, 2):
            if j == 2 or j == 3 or j == 5 or j == 7:
                print(f'{i} {j} {k}')