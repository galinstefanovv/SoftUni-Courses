m = int(input())
count = 0
found = ""
for a in range(1, 9 + 1):
    for b in range(1, 9 + 1):
        for c in range(1, 9 + 1):
            for d in range(1, 9 + 1):
                if a < b and c > d:
                    sums = (a * b) + (c * d)
                    if sums == m:
                        count += 1
                        print(f'{a}{b}{c}{d}')
                        print(count)



