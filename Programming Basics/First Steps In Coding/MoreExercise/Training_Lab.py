width = float(input())
height = float(input())
places = ((height * 100) - 100) // 70
rows = (width * 100) // 120
total = rows * places - 3
print(total)

