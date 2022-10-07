book = input()
search = input()
count = 0
found = False
while search != "No More Books":
    if search == book:
        found = True
        break
    count += 1
    search = input()
if found:
    print(f'You checked {count} books and found it.')
else:
    print(f'The book you search is not here!')
    print(f'You checked {count} books.')