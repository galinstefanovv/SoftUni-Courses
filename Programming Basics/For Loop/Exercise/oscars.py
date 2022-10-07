name = input()
points = float(input())
count = int(input())
total_points = 0
for persons in range (1, count + 1):
    p_name = input()
    p_points = float(input())
    t_points = (len(p_name) * p_points) / 2
    total_points += t_points
    if total_points + points > 1250.5:
        break

if total_points + points > 1250.5:
    print(f'Congratulations, {name} got a nominee for leading role with {total_points + points:.1f}!')
else:
    diff = abs(total_points + points - 1250.5)
    print(f'Sorry, {name} you need {diff:.1f} more!')
