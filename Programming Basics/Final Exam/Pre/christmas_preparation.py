paper = int(input()) * 5.80
plat = int(input()) * 7.20
glue = float(input()) * 1.20
discount = int(input()) / 100
total = paper + plat + glue
total_discount = total - (total * discount)
print(f'{total_discount:.3f}')

