season = input()
group = input()
students = int(input())
days = int(input())
price = 0
sport = ""
if season == "Winter":
    if group == "boys":
        sport = "Judo"
        price = days * 9.60
    elif group == "girls":
        sport = "Gymnastics"
        price = days * 9.60
    elif group == "mixed":
        sport = "Ski"
        price = days * 10
    else:
        print("Invalid data!")

elif season == "Spring":
    if group == "boys":
        sport = "Tennis"
        price = days * 7.20
    elif group == "girls":
        sport = "Athletics"
        price = days * 7.20
    elif group == "mixed":
        sport = "Cycling"
        price = days * 9.50
    else:
        print("Invalid data!")

elif season == "Summer":
    if group == "boys":
        sport = "Football"
        price = days * 15
    elif group == "girls":
        sport = "Volleyball"
        price = days * 15
    elif group == "mixed":
        sport = "Swimming"
        price = days * 20
    else:
        print("Invalid data!")
else:
    print("Invalid data!")

price *= students

if students >= 50:
    price = price - (price * 0.5)
elif 20 <= students < 50:
    price = price - (price * 0.15)
elif 10 <= students < 20:
    price = price - (price * 0.05)
print(f'{sport} {price:.2f} lv.')


