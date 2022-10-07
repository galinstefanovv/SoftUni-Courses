start = int(input())
end = int(input())
magic_number = int(input())
count = 0
sum = 0
found = False
for i in range(start, end + 1):
    for k in range(start, end + 1):
        count += 1
        if i + k == magic_number:
            print(f'Combination N:{count} ({i} + {k} = {magic_number})')
            found = True
            break
        if found:
            break
    if found:
        break
if not found:
    print(f'{count} combinations - neither equals {magic_number}')
