n = int(input())
input_line = input()
count = 0
total = 0
count_grade = 0
while input_line != "Finish":
    presentation = input_line
    sum = 0
    count += 1
    for i in range(1, n + 1):
        grade = float(input())
        count_grade += 1
        sum += grade
        total += grade
    average = sum / n
    print(f'{presentation} - {average:.2f}.')
    input_line = input()
print(f"Student's final assessment is {total / count_grade:.2f}.")