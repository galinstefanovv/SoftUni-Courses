months = int(input())
electricity = 0
for i in range(1, months + 1):
    electricity_bill = float(input())
    electricity = electricity + electricity_bill
water = months * 20
internet = months * 15
other = electricity + water + internet
other_price = other + (other * 0.2)
average = (electricity + water + internet + other_price) / months
print(f'Electricity: {electricity:.2f} lv')
print(f'Water: {water:.2f} lv')
print(f'Internet: {internet:.2f} lv')
print(f'Other: {other_price:.2f} lv')
print(f'Average: {average:.2f} lv')