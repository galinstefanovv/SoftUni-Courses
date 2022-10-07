total_pen = int(input()) * 5.80
total_mark = int(input()) * 7.20
liquid_lt = int(input()) * 1.20
discount = int(input()) / 100
price = total_pen + total_mark + liquid_lt
solution = price - (price * discount)
print(solution)

