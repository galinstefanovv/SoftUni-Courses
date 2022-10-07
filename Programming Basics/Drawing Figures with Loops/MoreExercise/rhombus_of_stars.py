n = int(input())

for row in range(1, n + 1):
    for col in range(1, n - row + 1):
        print(' ', end='')
    print('*', end='')
    for col in range(1, row):
        print(' *', end='')
    print()

    
for row2 in range(n - 1, 0, -1):
    for col1 in range(1, n - row2 + 1):
        print(' ', end='')
    print('*', end='')
    for col1 in range(1, row2):
        print(' *', end='')
    print()