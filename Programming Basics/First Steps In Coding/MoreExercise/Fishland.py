mackerel_price = float(input()) # skumriq cena
sprat_price = float(input()) # caca
bonito_kg = float(input()) # palamud
horse_mackerel_kg = float(input()) #safrid
mussels_kg = int(input()) # midi

bonito_price = mackerel_price + (mackerel_price * 0.6)
bonito_price_total = bonito_price * bonito_kg
horse_mackerel_price = sprat_price + (sprat_price * 0.8)
horse_mackerel_total = horse_mackerel_price * horse_mackerel_kg
mussels_price = mussels_kg * 7.50

total = bonito_price_total + horse_mackerel_total + mussels_price
print(f'{total:.2f}')




