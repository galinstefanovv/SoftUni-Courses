text = input()
total = 0

for char in text:
    if char == "a":
        total = total + 1
    if char == "e":
        total = total + 2
    if char == "i":
        total = total + 3
    if char == "o":
        total = total + 4
    if char == "u":
        total = total + 5
print(total)
