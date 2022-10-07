input_line = input()
count = 1
total = 5364
reached = False
days_over = False
while input_line != "END":
    meters = int(input())
    if input_line == "Yes":
        count += 1
        if count > 5:
            break
        total += meters
    else:
        total += meters
    if total >= 8848:
        reached = True
        break
    input_line = input()


if reached:
    print(f'Goal reached for {count} days!')
else:
    print('Failed!')
    print(f'{total}')