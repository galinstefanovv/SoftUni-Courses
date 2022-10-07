n1 = int(input())
n2 = int(input())
operator = input()
total = 0

if operator == "+" or operator == "-" or operator == "*":
    if operator == "+":
        total = n1 + n2
    elif operator == "-":
        total = n1 - n2
    else:
        total = n1 * n2
    if total % 2 == 0:
        typ = "even"
    else:
        typ = "odd"
    print(f'{n1} {operator} {n2} = {total} - {typ}')
elif operator == "/":
    if n1 == 0 or n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        total = n1 / n2
        print(f'{n1} / {n2} = {total:.2f}')
elif operator == "%":
    if n1 == 0 or n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        total = n1 % n2
        print(f'{n1} % {n2} = {total}')
else:
    print("Invalid operator")
