funds = int(input())
charity = input()
count = 0
sums = 0
cash = 0
card = 0
card_ave = 0
cash_ave = 0
done = False
while True:
    if charity == "End":
        print("Failed to collect required money for charity.")
        break
    funds_amount = int(charity)
    count += 1
    if count % 2 == 0:
        if funds_amount < 10:
            print("Error in transaction!")
        else:
            print("Product sold!")
            sums += funds_amount
            card_ave += funds_amount
            card += 1
    else:
        if funds_amount > 100:
            print("Error in transaction!")
        else:
            print("Product sold!")
            sums += funds_amount
            cash_ave += funds_amount
            cash += 1
    if sums >= funds:
        done = True
        break
    charity = input()

if done:
    average_card = card_ave / card
    average_cash = cash_ave / cash
    print(f"Average CS: {average_cash:.2f}")
    print(f"Average CC: {average_card:.2f}")