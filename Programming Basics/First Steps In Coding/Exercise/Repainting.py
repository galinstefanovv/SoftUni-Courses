nylon_quant = (int(input()) + 2) * 1.5
paint_quant = int(input())  * 14.50
paint = paint_quant + (paint_quant * 0.1)
thinner_quant = int(input()) * 5
hours = int(input())
total = nylon_quant + paint + thinner_quant + 0.40
pay_maist = (total*0.3) * hours
solution = total + pay_maist
print(solution)



