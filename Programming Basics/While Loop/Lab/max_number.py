import sys
n = input()
max_num = -sys.maxsize
while n != "Stop":
    currentNum = int(n)
    if currentNum > max_num:
        max_num = currentNum
    n = input()
print(max_num)