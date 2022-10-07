from math import floor, ceil
magnolias = int(input()) * 3.25
hyacinth = int(input()) * 4
rose = int(input()) * 3.5
cacti = int(input()) * 8
gift_price = float(input())

price = magnolias + hyacinth + rose + cacti
tax = price * 0.05
price_tax = price - tax

diff = abs(gift_price - price_tax)

if price_tax >= gift_price:
    print(f'She is left with {floor(diff)} leva.')
else:
    print(f'She will have to borrow {ceil(diff)} leva.')
