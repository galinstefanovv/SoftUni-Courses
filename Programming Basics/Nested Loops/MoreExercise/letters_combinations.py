start = input()
end = input()
exceptl = input()
result = ""
count = 0
for i in range(ord(start), ord(end) + 1):
    if i == ord(exceptl):
        continue
    for j in range(ord(start), ord(end) + 1):
        if j == ord(exceptl):
            continue
        for k in range(ord(start), ord(end) + 1):
            if k == ord(exceptl):
                continue
            result += chr(i) + chr(j) + chr(k) + " "
            count += 1
print(f'{result}{count}')
