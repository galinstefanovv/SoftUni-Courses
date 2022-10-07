import sys
kilometers = int(input())
time_of_day = input()
price = 0
if time_of_day == "day":
    taxi = 0.79
elif time_of_day == "night":
    taxi = 0.9
else:
    sys.exit("Please enter 'day' or 'night'")
if 1 <= kilometers < 20:
    price = (kilometers*taxi) + 0.70
    print(f'{price:.2f}')
elif 20 <= kilometers < 100:
    price = kilometers * 0.09
    print(f'{price:.2f}')
else:
    price = kilometers * 0.06
    print(f'{price:.2f}')
