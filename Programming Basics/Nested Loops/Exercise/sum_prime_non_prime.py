input_line = input()
prime = 0
non_prime = 0
while input_line != "stop":
    new_line = int(input_line)
    if new_line < 0:
        print('Number is negative.')
        input_line = input()
        continue
    count = 0
    for i in range(1, new_line + 1):
        if new_line % i == 0:
            count += 1
    if count == 2:
        prime += new_line
    else:
        non_prime += new_line
    input_line = input()
print(f'Sum of all prime numbers is: {prime}')
print(f'Sum of all non prime numbers is: {non_prime}')