projection = input()
r = int(input())
c = int(input())
price = 0
seats = r * c

if projection == "Premiere":
    price = 12 * seats
elif projection == "Normal":
    price = 7.5 * seats
elif projection == "Discount":
    price = 5 * seats
else:
    print("Error")

print(f'{price:.2f} leva')