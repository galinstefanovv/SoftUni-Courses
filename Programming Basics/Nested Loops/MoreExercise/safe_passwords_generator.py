first = int(input())
second = int(input())
number = int(input())
count = 0
flag = False
for a in range(35, 55):
    for b in range(64, 96):
        for x in range(1, first + 1):
            for y in range(1, second + 1):
                count += 1
                if count > number:
                    flag = True
                    break
                print(f'{chr(a)}{chr(b)}{x}{y}{chr(b)}{chr(a)}', end="|")
                if x == first and y == second:
                    flag = True
                    break
                a += 1
                if a > 55:
                    a = 35
                b += 1
                if b > 96:
                    b = 64
            if flag:
                break
        if flag:
            break
    if flag:
        break
