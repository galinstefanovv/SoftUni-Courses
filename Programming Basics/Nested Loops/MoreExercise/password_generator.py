n = int(input())
l = int(input())

for first in range(1, n + 1):
    for second in range(1, n + 1):
        for third in range(97, 97 + l):
            for fourth in range(97, 97 + l):
                for five in range(1, n + 1):
                    if five > first and five > second:
                        print(f'{first}{second}{chr(third)}{chr(fourth)}{five}', end=" ")
