time = int(input())
weekday = input()
if weekday == "Monday" or weekday == "Tuesday" or weekday == "Wednesday" or weekday == "Thursday" \
        or weekday == "Friday" or weekday == "Saturday":
    if 10 <= time <= 18:
        print("open")
    else:
        print("closed")
else:
    print("closed")
