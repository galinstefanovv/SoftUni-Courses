budget = float(input())
card = int(input())
processor = int(input())
ram = int(input())
card_price = card * 250
processor_price = (card_price * 0.35) * processor
ram_price = (card_price * 0.1) * ram
total = card_price + processor_price + ram_price
if card > processor:
    total = total - (total*0.15)
if budget >= total:
    diff = budget - total
    print(f'You have {diff:.2f} leva left!')
else:
    diff = total - budget
    print(f'Not enough money! You need {diff:.2f} leva more!')