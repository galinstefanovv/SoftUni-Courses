import sys
n = int(input())
max_num = -sys.maxsize
min_num = sys.maxsize
max_num_even = -sys.maxsize
min_num_even = sys.maxsize
oddsum = 0
evensum = 0
for i in range(1, n + 1):
    number = float(input())
    if i % 2 == 0:
        evensum += number
        if number > max_num_even:
            max_num_even = number
        if number < min_num_even:
            min_num_even = number
    else:
        oddsum += number
        if number > max_num:
            max_num = number
        if number < min_num:
            min_num = number
print(f'OddSum={oddsum:.2f},')
if min_num != sys.maxsize:
    print(f'OddMin={min_num:.2f},')
else:
    print(f'OddMin=No,')
if max_num != -sys.maxsize:
    print(f'OddMax={max_num:.2f},')
else:
    print(f'OddMax=No,')

print(f'EvenSum={evensum:.2f},')
if min_num_even != sys.maxsize:
    print(f'EvenMin={min_num_even:.2f},')
else:
    print(f'EvenMin=No,')
if max_num_even != -sys.maxsize:
    print(f'EvenMax={max_num_even:.2f}')
else:
    print(f'EvenMax=No')