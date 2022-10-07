from math import pi

print("Please choose your figure: square, rectangle, circle or triangle.")
figure = input()
if figure == "square":
    print("Please write the size of the side.")
    print("a = ", end = ' ')
    number1 = float(input())
    area1 = number1*number1
    print(f'{area1:.3f}')
elif figure == "rectangle":
    print("Please write size of the two sides")
    print("a = ", end=' ')
    number2 = float(input())
    print("b = ", end=' ')
    number3 = float(input())
    area2 = number2*number3
    print(f'{area2:.3f}')
elif figure == "circle":
    print("Please write the size of the radius.")
    print("r = ", end=' ')
    number4 = float(input())
    area3 = pi * number4 * number4
    print(f'{area3:.3f}')
elif figure == "triangle":
    print("Please write 'a' and 'h'")
    print("a = ", end=' ')
    number5 = float(input())
    print("h = ", end=' ')
    number6 = float(input())
    area4 = (number5 * number6) / 2
    print(f'{area4:.3f}')
else:
    print("Wrong figure!")