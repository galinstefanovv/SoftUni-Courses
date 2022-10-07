n = int(input())
sum = 0
while True:
    numbers = int(input())
    sum += numbers
    if sum >= n:
        print(sum)
        break