students = int(input())
exc = 0
good = 0
mid = 0
fail = 0
average = 0
for i in range(1, students + 1):
    grade = float(input())
    average += grade
    if 2 <= grade <= 2.99:
        fail += 1
    elif 3 <= grade <= 3.99:
        mid += 1
    elif 4 <= grade <= 4.99:
        good += 1
    else:
        exc += 1
p1 = exc / students * 100
print(f'Top students: {p1:.2f}%')
p2 = good / students * 100
print(f'Between 4.00 and 4.99: {p2:.2f}%')
p3 = mid / students * 100
print(f'Between 3.00 and 3.99: {p3:.2f}%')
p4 = fail / students * 100
print(f'Fail: {p4:.2f}%')
p5 = (average / students)
print(f'Average: {p5:.2f}')

