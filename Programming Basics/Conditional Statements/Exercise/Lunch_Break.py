import math
serial = input()
ep_length = int(input())
rest = int(input())

lunch = rest * 1/8
relax = rest * 1/4

total = lunch + relax

sum = rest - total

if sum >= ep_length:
    diff = sum - ep_length
    print(f'You have enough time to watch {serial} and left with {math.ceil(diff)} minutes free time.')
else:
    diff = ep_length - sum
    print(f"You don't have enough time to watch {serial}, you need {math.ceil(diff)} more minutes.")
