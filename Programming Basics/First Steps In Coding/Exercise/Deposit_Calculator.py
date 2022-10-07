deposit_amount = float(input())
deposit_term = int(input())
annual_rate = float(input()) / 100
total = deposit_amount + deposit_term * ((deposit_amount * annual_rate) / 12)
print(total)