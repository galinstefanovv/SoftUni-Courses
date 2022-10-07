bad_grades = int(input())
exercise = input()
count = 0
bad = 0
sums = 0
failed = False
while exercise != "Enough":
    grade = int(input())
    if grade <= 4:
        bad += 1
        if bad >= bad_grades:
            failed = True
            break
    last_problem = exercise
    exercise = input()
    sums += grade
    count += 1
if failed:
    print(f'You need a break, {bad} poor grades.')
else:
    print(f'Average score: {sums / count:.2f}')
    print(f'Number of problems: {count}')
    print(f'Last problem: {last_problem}')