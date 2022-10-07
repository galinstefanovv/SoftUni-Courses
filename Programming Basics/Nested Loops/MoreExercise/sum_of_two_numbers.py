start = int(input())
end = int(input())
magic_number = int(input())
count = 0
found = False
for i in range(start, end + 1):
    for j in range(start ,end + 1):
        count += 1
        if i + j == magic_number:
            found = True
            break
    if i + j == magic_number:
        break

if found:
    print(f'Combination N:{count} ({i} + {j} = {magic_number})')
else:
    print(f'{count} combinations - neither equals {magic_number}')