sums = 0
n = input()

while n != "NoMoreMoney":
    current_sum = float(n)
    if current_sum >= 0:
        print(f'Increase: {current_sum:.2f}')
    else:
        print('Invalid operation!')
        break
    sums += current_sum
    n = input()

print(f'Total: {sums:.2f}')