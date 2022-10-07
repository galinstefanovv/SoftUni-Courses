rest = int(input())
days = 365 - rest
total_minutes = 30000
work = days * 63
not_work = rest * 127

playtime = work + not_work

if playtime > total_minutes:
    hours = (playtime - total_minutes) // 60
    minutes = (playtime - total_minutes)  % 60
    print(f'Tom will run away')
    print(f'{hours} hours and {minutes} minutes more for play')
else:
    hours = (total_minutes - playtime) // 60
    minutes = (total_minutes - playtime)  % 60
    print(f'Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')





