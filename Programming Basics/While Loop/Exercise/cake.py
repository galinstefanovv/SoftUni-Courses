width = int(input())
length = int(input())
pieces = input()
size = width * length
over = False
while pieces != "STOP":
    input_line = int(pieces)
    size -= input_line
    if size <= 0:
        over = True
        break
    pieces = input()
if over:
    print(f'No more cake left! You need {abs(size)} pieces more.')
else:
    print(f'{size} pieces are left.')