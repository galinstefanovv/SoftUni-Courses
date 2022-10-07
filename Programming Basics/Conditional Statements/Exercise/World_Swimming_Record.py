record = float(input())
distance_m = float(input())
seconds = float(input())

time = distance_m * seconds
slow = (distance_m // 15) * 12.5
total_time = time + slow
if total_time < record:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {total_time - record:.2f} seconds slower.')