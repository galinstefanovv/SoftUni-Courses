size = int(input()) * int(input()) * int(input())
boxes = input()
sums = 0
over = False
while boxes != "Done":
    boxes_count = int(boxes)
    sums += boxes_count
    if size <= sums:
        over = True
        break
    boxes = input()

diff = abs(size - sums)
if over:
    print(f'No more free space! You need {diff} Cubic meters more.')
else:
    print(f'{diff} Cubic meters left.')