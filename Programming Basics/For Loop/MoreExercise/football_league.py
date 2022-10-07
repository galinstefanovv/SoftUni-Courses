import sys
capacity = int(input())
fans = int(input())
a = 0
b = 0
v = 0
g = 0
for i in range(1, fans + 1):
    sector = input()

    if sector == "A":
        a += 1
    elif sector == "B":
        b += 1
    elif sector == "V":
        v += 1
    elif sector == "G":
        g += 1
    else:
        break
a = a / fans * 100
print(f'{a:.2f}%')
b = b / fans * 100
print(f'{b:.2f}%')
v = v / fans * 100
print(f'{v:.2f}%')
g = g / fans * 100
print(f'{g:.2f}%')
percentage = fans / capacity * 100
print(f'{percentage:.2f}%')


