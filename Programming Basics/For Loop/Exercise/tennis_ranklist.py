from math import floor

tournaments = int(input())
start_points = int(input())
points = 0
wins = 0
for count in range(1, tournaments + 1):
    stage = input()
    if stage == "W":
        points += 2000
        wins += 1
    elif stage == "F":
        points += 1200
    elif stage == "SF":
        points += 720

final_points = start_points + points
average_points = points / tournaments
percentage = (wins / tournaments) * 100

print(f'Final points: {final_points}')
print(f'Average points: {floor(average_points)}')
print(f'{percentage:.2f}%')

