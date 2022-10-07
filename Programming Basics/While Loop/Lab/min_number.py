import sys
n = input()
min_num = sys.maxsize
while n != "Stop":
    currentNum = int(n)
    if currentNum < min_num:
        min_num = currentNum
    n = input()
print(min_num)