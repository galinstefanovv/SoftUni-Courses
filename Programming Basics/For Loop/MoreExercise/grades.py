students = int(input())
count = 0
count1 = 0
count2 = 0
count3 = 0
total = 0
for grades in range(1, students + 1):
    grade = float(input())
    total += grade
    if grade <= 2.99:
        count += 1
    elif grade <= 3.99:
        count1 += 1
    elif grade <= 4.99:
        count2 += 1
    else:
        count3 += 1

top = count3 / students * 100
print(f'Top students: {top:.2f}%')
four = count2 / students * 100
print(f'Between 4.00 and 4.99: {four:.2f}%')
three = count1 / students * 100
print(f'Between 3.00 and 3.99: {three:.2f}%')
fail = count / students * 100
print(f'Fail: {fail:.2f}%')
average = total / students
print(f'Average: {average:.2f}')
